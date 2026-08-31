from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_run_discovery_create_actual_availability_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_alternative_name_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_annotations_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_archived_at_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_archived_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateArchivedErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_archived_reason_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_backup_enabled_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_criticality_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_debug_mode_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_description_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_discovery_enabled_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_display_name_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_encrypted_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateEncryptedErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_endpoint_monitors_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_gitlab_project_id_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_gitlab_project_url_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_kind_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateKindErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_labels_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateLabelsErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_name_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateNameErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_non_field_errors_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_notifications_enabled_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_on_premise_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_organization_id_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_owner_id_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_platform_service_error_component import (
        ApiV1WorkspacesRunDiscoveryCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_pop_id_error_component import (
        ApiV1WorkspacesRunDiscoveryCreatePopIdErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_provider_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateProviderErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_provider_id_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_provider_reference_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_purpose_error_component import (
        ApiV1WorkspacesRunDiscoveryCreatePurposeErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_readme_md_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateReadmeMdErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_reconciliation_enabled_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_scope_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_secrets_poly_raw_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_sla_availability_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_sla_target_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_slo_availability_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_slo_target_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_target_availability_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_template_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateTemplateErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_urls_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateUrlsErrorComponent,
    )
    from ..models.api_v1_workspaces_run_discovery_create_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesRunDiscoveryCreateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesRunDiscoveryCreateValidationError")


@_attrs_define
class ApiV1WorkspacesRunDiscoveryCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesRunDiscoveryCreateActualAvailabilityErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateAlternativeNameErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateArchivedAtErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateArchivedErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateArchivedReasonErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateBackupEnabledErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateCriticalityErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateDebugModeErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateDescriptionErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateDiscoveryEnabledErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateDisplayNameErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateEncryptedErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateEndpointMonitoringModeErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateEndpointMonitorsErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateGitlabProjectIdErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateHasIncompatibleKubeconfigErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateKindErrorComponent | ApiV1WorkspacesRunDiscoveryCreateLabelsErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateNameErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateNonFieldErrorsErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateNotificationsEnabledErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateOnPremiseErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateOrganizationIdErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateOwnerIdErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreatePlatformServiceErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreatePopIdErrorComponent | ApiV1WorkspacesRunDiscoveryCreateProviderErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateProviderIdErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateProviderReferenceErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreatePurposeErrorComponent | ApiV1WorkspacesRunDiscoveryCreateReadmeMdErrorComponent
            | ApiV1WorkspacesRunDiscoveryCreateReconciliationEnabledErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateSecretsPolyRawErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateSlaAvailabilityErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateSlaTargetErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateSloAvailabilityErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateSloTargetErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateTargetAvailabilityErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateTemplateErrorComponent | ApiV1WorkspacesRunDiscoveryCreateUrlsErrorComponent |
            ApiV1WorkspacesRunDiscoveryCreateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesRunDiscoveryCreateActualAvailabilityErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateAlternativeNameErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateArchivedAtErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateArchivedErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateArchivedReasonErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateBackupEnabledErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateCriticalityErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateDebugModeErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateDescriptionErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateDisplayNameErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateEncryptedErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateKindErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateLabelsErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateNameErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateOnPremiseErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateOrganizationIdErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateOwnerIdErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreatePlatformServiceErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreatePopIdErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateProviderErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateProviderIdErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateProviderReferenceErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreatePurposeErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateReadmeMdErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateSlaTargetErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateSloAvailabilityErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateSloTargetErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateTemplateErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateUrlsErrorComponent
        | ApiV1WorkspacesRunDiscoveryCreateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_run_discovery_create_actual_availability_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_annotations_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_archived_at_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_archived_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_archived_reason_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_backup_enabled_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_criticality_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_debug_mode_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_description_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_discovery_enabled_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_display_name_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_encrypted_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_kind_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_labels_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_name_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_non_field_errors_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_notifications_enabled_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_on_premise_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_organization_id_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_owner_id_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_platform_service_error_component import (
            ApiV1WorkspacesRunDiscoveryCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_pop_id_error_component import (
            ApiV1WorkspacesRunDiscoveryCreatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_provider_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_provider_id_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_provider_reference_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_purpose_error_component import (
            ApiV1WorkspacesRunDiscoveryCreatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_readme_md_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_scope_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_sla_availability_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_sla_target_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_slo_availability_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_slo_target_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_target_availability_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_template_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_urls_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateWorkspaceInventoryRawErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateGitlabProjectUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateGlobalEndpointMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesRunDiscoveryCreateMonitoringWorkspaceAllowlistIdsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateNotificationsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateBackupEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateHasIncompatibleKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateEndpointMonitorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateSecretsPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateWorkspaceInventoryRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRunDiscoveryCreateReadmeMdErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_workspaces_run_discovery_create_actual_availability_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_alternative_name_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateAlternativeNameErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_annotations_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_archived_at_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_archived_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_archived_reason_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_backup_enabled_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_criticality_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_debug_mode_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_description_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_discovery_enabled_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_display_name_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_encrypted_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_kind_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_labels_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_name_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_non_field_errors_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_notifications_enabled_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_on_premise_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_organization_id_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_owner_id_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_platform_service_error_component import (
            ApiV1WorkspacesRunDiscoveryCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_pop_id_error_component import (
            ApiV1WorkspacesRunDiscoveryCreatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_provider_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_provider_id_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_provider_reference_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_purpose_error_component import (
            ApiV1WorkspacesRunDiscoveryCreatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_readme_md_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_scope_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_sla_availability_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_sla_target_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_slo_availability_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_slo_target_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_target_availability_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_template_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_urls_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_run_discovery_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesRunDiscoveryCreateWorkspaceInventoryRawErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesRunDiscoveryCreateActualAvailabilityErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateAlternativeNameErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateArchivedAtErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateArchivedErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateArchivedReasonErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateBackupEnabledErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateCriticalityErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateDebugModeErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateDescriptionErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateDisplayNameErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateEncryptedErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateKindErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateLabelsErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateNameErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateOnPremiseErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateOrganizationIdErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateOwnerIdErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreatePlatformServiceErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreatePopIdErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateProviderErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateProviderIdErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateProviderReferenceErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreatePurposeErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateReadmeMdErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateSlaTargetErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateSloAvailabilityErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateSloTargetErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateTemplateErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateUrlsErrorComponent
                | ApiV1WorkspacesRunDiscoveryCreateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_0 = (
                        ApiV1WorkspacesRunDiscoveryCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_1 = (
                        ApiV1WorkspacesRunDiscoveryCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_2 = (
                        ApiV1WorkspacesRunDiscoveryCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_3 = (
                        ApiV1WorkspacesRunDiscoveryCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_4 = (
                        ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_5 = (
                        ApiV1WorkspacesRunDiscoveryCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_6 = (
                        ApiV1WorkspacesRunDiscoveryCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_7 = (
                        ApiV1WorkspacesRunDiscoveryCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_8 = (
                        ApiV1WorkspacesRunDiscoveryCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_9 = (
                        ApiV1WorkspacesRunDiscoveryCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_10 = (
                        ApiV1WorkspacesRunDiscoveryCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_11 = (
                        ApiV1WorkspacesRunDiscoveryCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_12 = (
                        ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_13 = (
                        ApiV1WorkspacesRunDiscoveryCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_14 = (
                        ApiV1WorkspacesRunDiscoveryCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_15 = (
                        ApiV1WorkspacesRunDiscoveryCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_16 = (
                        ApiV1WorkspacesRunDiscoveryCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_17 = (
                        ApiV1WorkspacesRunDiscoveryCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_18 = (
                        ApiV1WorkspacesRunDiscoveryCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_19 = (
                        ApiV1WorkspacesRunDiscoveryCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_20 = (
                        ApiV1WorkspacesRunDiscoveryCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_21 = (
                        ApiV1WorkspacesRunDiscoveryCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_22 = (
                        ApiV1WorkspacesRunDiscoveryCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_23 = (
                        ApiV1WorkspacesRunDiscoveryCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_24 = (
                        ApiV1WorkspacesRunDiscoveryCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_25 = (
                        ApiV1WorkspacesRunDiscoveryCreateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_26 = (
                        ApiV1WorkspacesRunDiscoveryCreateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_27 = (
                        ApiV1WorkspacesRunDiscoveryCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_28 = (
                        ApiV1WorkspacesRunDiscoveryCreateGlobalEndpointMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_29 = (
                        ApiV1WorkspacesRunDiscoveryCreateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_30 = (
                        ApiV1WorkspacesRunDiscoveryCreateNotificationsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_31 = (
                        ApiV1WorkspacesRunDiscoveryCreateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_32 = (
                        ApiV1WorkspacesRunDiscoveryCreateHasIncompatibleKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_33 = (
                        ApiV1WorkspacesRunDiscoveryCreateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_34 = (
                        ApiV1WorkspacesRunDiscoveryCreateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_35 = (
                        ApiV1WorkspacesRunDiscoveryCreateWorkspaceInventoryRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_36 = (
                        ApiV1WorkspacesRunDiscoveryCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_37 = (
                        ApiV1WorkspacesRunDiscoveryCreateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_38 = (
                        ApiV1WorkspacesRunDiscoveryCreatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_39 = (
                        ApiV1WorkspacesRunDiscoveryCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_40 = (
                        ApiV1WorkspacesRunDiscoveryCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_41 = (
                        ApiV1WorkspacesRunDiscoveryCreatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_42 = (
                        ApiV1WorkspacesRunDiscoveryCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_43 = (
                        ApiV1WorkspacesRunDiscoveryCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_run_discovery_create_error_type_44 = (
                        ApiV1WorkspacesRunDiscoveryCreateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_run_discovery_create_error_type_45 = (
                    ApiV1WorkspacesRunDiscoveryCreateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_run_discovery_create_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_run_discovery_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_run_discovery_create_validation_error.additional_properties = d
        return api_v1_workspaces_run_discovery_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
