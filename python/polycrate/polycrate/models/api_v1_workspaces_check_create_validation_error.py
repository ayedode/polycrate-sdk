from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_check_create_actual_availability_error_component import (
        ApiV1WorkspacesCheckCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_alternative_name_error_component import (
        ApiV1WorkspacesCheckCreateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_annotations_error_component import (
        ApiV1WorkspacesCheckCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_archived_at_error_component import (
        ApiV1WorkspacesCheckCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_archived_error_component import (
        ApiV1WorkspacesCheckCreateArchivedErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_archived_reason_error_component import (
        ApiV1WorkspacesCheckCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_backup_enabled_error_component import (
        ApiV1WorkspacesCheckCreateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_criticality_error_component import (
        ApiV1WorkspacesCheckCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_debug_mode_error_component import (
        ApiV1WorkspacesCheckCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_description_error_component import (
        ApiV1WorkspacesCheckCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_discovery_enabled_error_component import (
        ApiV1WorkspacesCheckCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_display_name_error_component import (
        ApiV1WorkspacesCheckCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_encrypted_error_component import (
        ApiV1WorkspacesCheckCreateEncryptedErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesCheckCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_endpoint_monitors_error_component import (
        ApiV1WorkspacesCheckCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_gitlab_project_id_error_component import (
        ApiV1WorkspacesCheckCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_gitlab_project_url_error_component import (
        ApiV1WorkspacesCheckCreateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesCheckCreateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesCheckCreateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_kind_error_component import (
        ApiV1WorkspacesCheckCreateKindErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_labels_error_component import (
        ApiV1WorkspacesCheckCreateLabelsErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesCheckCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_name_error_component import (
        ApiV1WorkspacesCheckCreateNameErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_non_field_errors_error_component import (
        ApiV1WorkspacesCheckCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_notifications_enabled_error_component import (
        ApiV1WorkspacesCheckCreateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_on_premise_error_component import (
        ApiV1WorkspacesCheckCreateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_organization_id_error_component import (
        ApiV1WorkspacesCheckCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_owner_id_error_component import (
        ApiV1WorkspacesCheckCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_platform_service_error_component import (
        ApiV1WorkspacesCheckCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_pop_id_error_component import (
        ApiV1WorkspacesCheckCreatePopIdErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_provider_error_component import (
        ApiV1WorkspacesCheckCreateProviderErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_provider_id_error_component import (
        ApiV1WorkspacesCheckCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_provider_reference_error_component import (
        ApiV1WorkspacesCheckCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_purpose_error_component import (
        ApiV1WorkspacesCheckCreatePurposeErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_readme_md_error_component import (
        ApiV1WorkspacesCheckCreateReadmeMdErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_reconciliation_enabled_error_component import (
        ApiV1WorkspacesCheckCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_scope_error_component import (
        ApiV1WorkspacesCheckCreateScopeErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_secrets_poly_raw_error_component import (
        ApiV1WorkspacesCheckCreateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_sla_availability_error_component import (
        ApiV1WorkspacesCheckCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_sla_target_error_component import (
        ApiV1WorkspacesCheckCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_slo_availability_error_component import (
        ApiV1WorkspacesCheckCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_slo_target_error_component import (
        ApiV1WorkspacesCheckCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_target_availability_error_component import (
        ApiV1WorkspacesCheckCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_template_error_component import (
        ApiV1WorkspacesCheckCreateTemplateErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_urls_error_component import (
        ApiV1WorkspacesCheckCreateUrlsErrorComponent,
    )
    from ..models.api_v1_workspaces_check_create_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesCheckCreateValidationError")


@_attrs_define
class ApiV1WorkspacesCheckCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesCheckCreateActualAvailabilityErrorComponent |
            ApiV1WorkspacesCheckCreateAlternativeNameErrorComponent | ApiV1WorkspacesCheckCreateAnnotationsErrorComponent |
            ApiV1WorkspacesCheckCreateArchivedAtErrorComponent | ApiV1WorkspacesCheckCreateArchivedErrorComponent |
            ApiV1WorkspacesCheckCreateArchivedReasonErrorComponent | ApiV1WorkspacesCheckCreateBackupEnabledErrorComponent |
            ApiV1WorkspacesCheckCreateCriticalityErrorComponent | ApiV1WorkspacesCheckCreateDebugModeErrorComponent |
            ApiV1WorkspacesCheckCreateDescriptionErrorComponent | ApiV1WorkspacesCheckCreateDiscoveryEnabledErrorComponent |
            ApiV1WorkspacesCheckCreateDisplayNameErrorComponent | ApiV1WorkspacesCheckCreateEncryptedErrorComponent |
            ApiV1WorkspacesCheckCreateEndpointMonitoringModeErrorComponent |
            ApiV1WorkspacesCheckCreateEndpointMonitorsErrorComponent |
            ApiV1WorkspacesCheckCreateGitlabProjectIdErrorComponent |
            ApiV1WorkspacesCheckCreateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesCheckCreateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesCheckCreateHasIncompatibleKubeconfigErrorComponent | ApiV1WorkspacesCheckCreateKindErrorComponent
            | ApiV1WorkspacesCheckCreateLabelsErrorComponent |
            ApiV1WorkspacesCheckCreateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesCheckCreateNameErrorComponent | ApiV1WorkspacesCheckCreateNonFieldErrorsErrorComponent |
            ApiV1WorkspacesCheckCreateNotificationsEnabledErrorComponent | ApiV1WorkspacesCheckCreateOnPremiseErrorComponent
            | ApiV1WorkspacesCheckCreateOrganizationIdErrorComponent | ApiV1WorkspacesCheckCreateOwnerIdErrorComponent |
            ApiV1WorkspacesCheckCreatePlatformServiceErrorComponent | ApiV1WorkspacesCheckCreatePopIdErrorComponent |
            ApiV1WorkspacesCheckCreateProviderErrorComponent | ApiV1WorkspacesCheckCreateProviderIdErrorComponent |
            ApiV1WorkspacesCheckCreateProviderReferenceErrorComponent | ApiV1WorkspacesCheckCreatePurposeErrorComponent |
            ApiV1WorkspacesCheckCreateReadmeMdErrorComponent | ApiV1WorkspacesCheckCreateReconciliationEnabledErrorComponent
            | ApiV1WorkspacesCheckCreateScopeErrorComponent | ApiV1WorkspacesCheckCreateSecretsPolyRawErrorComponent |
            ApiV1WorkspacesCheckCreateSlaAvailabilityErrorComponent | ApiV1WorkspacesCheckCreateSlaTargetErrorComponent |
            ApiV1WorkspacesCheckCreateSloAvailabilityErrorComponent | ApiV1WorkspacesCheckCreateSloTargetErrorComponent |
            ApiV1WorkspacesCheckCreateTargetAvailabilityErrorComponent | ApiV1WorkspacesCheckCreateTemplateErrorComponent |
            ApiV1WorkspacesCheckCreateUrlsErrorComponent | ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesCheckCreateActualAvailabilityErrorComponent
        | ApiV1WorkspacesCheckCreateAlternativeNameErrorComponent
        | ApiV1WorkspacesCheckCreateAnnotationsErrorComponent
        | ApiV1WorkspacesCheckCreateArchivedAtErrorComponent
        | ApiV1WorkspacesCheckCreateArchivedErrorComponent
        | ApiV1WorkspacesCheckCreateArchivedReasonErrorComponent
        | ApiV1WorkspacesCheckCreateBackupEnabledErrorComponent
        | ApiV1WorkspacesCheckCreateCriticalityErrorComponent
        | ApiV1WorkspacesCheckCreateDebugModeErrorComponent
        | ApiV1WorkspacesCheckCreateDescriptionErrorComponent
        | ApiV1WorkspacesCheckCreateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesCheckCreateDisplayNameErrorComponent
        | ApiV1WorkspacesCheckCreateEncryptedErrorComponent
        | ApiV1WorkspacesCheckCreateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesCheckCreateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesCheckCreateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesCheckCreateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesCheckCreateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesCheckCreateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesCheckCreateKindErrorComponent
        | ApiV1WorkspacesCheckCreateLabelsErrorComponent
        | ApiV1WorkspacesCheckCreateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesCheckCreateNameErrorComponent
        | ApiV1WorkspacesCheckCreateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesCheckCreateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesCheckCreateOnPremiseErrorComponent
        | ApiV1WorkspacesCheckCreateOrganizationIdErrorComponent
        | ApiV1WorkspacesCheckCreateOwnerIdErrorComponent
        | ApiV1WorkspacesCheckCreatePlatformServiceErrorComponent
        | ApiV1WorkspacesCheckCreatePopIdErrorComponent
        | ApiV1WorkspacesCheckCreateProviderErrorComponent
        | ApiV1WorkspacesCheckCreateProviderIdErrorComponent
        | ApiV1WorkspacesCheckCreateProviderReferenceErrorComponent
        | ApiV1WorkspacesCheckCreatePurposeErrorComponent
        | ApiV1WorkspacesCheckCreateReadmeMdErrorComponent
        | ApiV1WorkspacesCheckCreateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesCheckCreateScopeErrorComponent
        | ApiV1WorkspacesCheckCreateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesCheckCreateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesCheckCreateSlaTargetErrorComponent
        | ApiV1WorkspacesCheckCreateSloAvailabilityErrorComponent
        | ApiV1WorkspacesCheckCreateSloTargetErrorComponent
        | ApiV1WorkspacesCheckCreateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesCheckCreateTemplateErrorComponent
        | ApiV1WorkspacesCheckCreateUrlsErrorComponent
        | ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_check_create_actual_availability_error_component import (
            ApiV1WorkspacesCheckCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_annotations_error_component import (
            ApiV1WorkspacesCheckCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_archived_at_error_component import (
            ApiV1WorkspacesCheckCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_archived_error_component import (
            ApiV1WorkspacesCheckCreateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_archived_reason_error_component import (
            ApiV1WorkspacesCheckCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_backup_enabled_error_component import (
            ApiV1WorkspacesCheckCreateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_criticality_error_component import (
            ApiV1WorkspacesCheckCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_debug_mode_error_component import (
            ApiV1WorkspacesCheckCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_description_error_component import (
            ApiV1WorkspacesCheckCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_discovery_enabled_error_component import (
            ApiV1WorkspacesCheckCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_display_name_error_component import (
            ApiV1WorkspacesCheckCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_encrypted_error_component import (
            ApiV1WorkspacesCheckCreateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesCheckCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesCheckCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesCheckCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesCheckCreateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesCheckCreateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesCheckCreateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_kind_error_component import (
            ApiV1WorkspacesCheckCreateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_labels_error_component import (
            ApiV1WorkspacesCheckCreateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesCheckCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_name_error_component import (
            ApiV1WorkspacesCheckCreateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_non_field_errors_error_component import (
            ApiV1WorkspacesCheckCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_notifications_enabled_error_component import (
            ApiV1WorkspacesCheckCreateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_on_premise_error_component import (
            ApiV1WorkspacesCheckCreateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_organization_id_error_component import (
            ApiV1WorkspacesCheckCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_owner_id_error_component import (
            ApiV1WorkspacesCheckCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_platform_service_error_component import (
            ApiV1WorkspacesCheckCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_pop_id_error_component import (
            ApiV1WorkspacesCheckCreatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_provider_error_component import (
            ApiV1WorkspacesCheckCreateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_provider_id_error_component import (
            ApiV1WorkspacesCheckCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_provider_reference_error_component import (
            ApiV1WorkspacesCheckCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_purpose_error_component import (
            ApiV1WorkspacesCheckCreatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_readme_md_error_component import (
            ApiV1WorkspacesCheckCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesCheckCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_scope_error_component import (
            ApiV1WorkspacesCheckCreateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesCheckCreateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_sla_availability_error_component import (
            ApiV1WorkspacesCheckCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_sla_target_error_component import (
            ApiV1WorkspacesCheckCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_slo_availability_error_component import (
            ApiV1WorkspacesCheckCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_slo_target_error_component import (
            ApiV1WorkspacesCheckCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_target_availability_error_component import (
            ApiV1WorkspacesCheckCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_template_error_component import (
            ApiV1WorkspacesCheckCreateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_urls_error_component import (
            ApiV1WorkspacesCheckCreateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesCheckCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateGitlabProjectUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateGlobalEndpointMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateMonitoringWorkspaceAllowlistIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateNotificationsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateBackupEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateHasIncompatibleKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateEndpointMonitorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateSecretsPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCheckCreateReadmeMdErrorComponent):
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
        from ..models.api_v1_workspaces_check_create_actual_availability_error_component import (
            ApiV1WorkspacesCheckCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_alternative_name_error_component import (
            ApiV1WorkspacesCheckCreateAlternativeNameErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_annotations_error_component import (
            ApiV1WorkspacesCheckCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_archived_at_error_component import (
            ApiV1WorkspacesCheckCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_archived_error_component import (
            ApiV1WorkspacesCheckCreateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_archived_reason_error_component import (
            ApiV1WorkspacesCheckCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_backup_enabled_error_component import (
            ApiV1WorkspacesCheckCreateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_criticality_error_component import (
            ApiV1WorkspacesCheckCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_debug_mode_error_component import (
            ApiV1WorkspacesCheckCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_description_error_component import (
            ApiV1WorkspacesCheckCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_discovery_enabled_error_component import (
            ApiV1WorkspacesCheckCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_display_name_error_component import (
            ApiV1WorkspacesCheckCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_encrypted_error_component import (
            ApiV1WorkspacesCheckCreateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesCheckCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesCheckCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesCheckCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesCheckCreateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesCheckCreateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesCheckCreateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_kind_error_component import (
            ApiV1WorkspacesCheckCreateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_labels_error_component import (
            ApiV1WorkspacesCheckCreateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesCheckCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_name_error_component import (
            ApiV1WorkspacesCheckCreateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_non_field_errors_error_component import (
            ApiV1WorkspacesCheckCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_notifications_enabled_error_component import (
            ApiV1WorkspacesCheckCreateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_on_premise_error_component import (
            ApiV1WorkspacesCheckCreateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_organization_id_error_component import (
            ApiV1WorkspacesCheckCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_owner_id_error_component import (
            ApiV1WorkspacesCheckCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_platform_service_error_component import (
            ApiV1WorkspacesCheckCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_pop_id_error_component import (
            ApiV1WorkspacesCheckCreatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_provider_error_component import (
            ApiV1WorkspacesCheckCreateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_provider_id_error_component import (
            ApiV1WorkspacesCheckCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_provider_reference_error_component import (
            ApiV1WorkspacesCheckCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_purpose_error_component import (
            ApiV1WorkspacesCheckCreatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_readme_md_error_component import (
            ApiV1WorkspacesCheckCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesCheckCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_scope_error_component import (
            ApiV1WorkspacesCheckCreateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesCheckCreateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_sla_availability_error_component import (
            ApiV1WorkspacesCheckCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_sla_target_error_component import (
            ApiV1WorkspacesCheckCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_slo_availability_error_component import (
            ApiV1WorkspacesCheckCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_slo_target_error_component import (
            ApiV1WorkspacesCheckCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_target_availability_error_component import (
            ApiV1WorkspacesCheckCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_template_error_component import (
            ApiV1WorkspacesCheckCreateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_urls_error_component import (
            ApiV1WorkspacesCheckCreateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_check_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesCheckCreateActualAvailabilityErrorComponent
                | ApiV1WorkspacesCheckCreateAlternativeNameErrorComponent
                | ApiV1WorkspacesCheckCreateAnnotationsErrorComponent
                | ApiV1WorkspacesCheckCreateArchivedAtErrorComponent
                | ApiV1WorkspacesCheckCreateArchivedErrorComponent
                | ApiV1WorkspacesCheckCreateArchivedReasonErrorComponent
                | ApiV1WorkspacesCheckCreateBackupEnabledErrorComponent
                | ApiV1WorkspacesCheckCreateCriticalityErrorComponent
                | ApiV1WorkspacesCheckCreateDebugModeErrorComponent
                | ApiV1WorkspacesCheckCreateDescriptionErrorComponent
                | ApiV1WorkspacesCheckCreateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesCheckCreateDisplayNameErrorComponent
                | ApiV1WorkspacesCheckCreateEncryptedErrorComponent
                | ApiV1WorkspacesCheckCreateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesCheckCreateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesCheckCreateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesCheckCreateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesCheckCreateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesCheckCreateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesCheckCreateKindErrorComponent
                | ApiV1WorkspacesCheckCreateLabelsErrorComponent
                | ApiV1WorkspacesCheckCreateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesCheckCreateNameErrorComponent
                | ApiV1WorkspacesCheckCreateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesCheckCreateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesCheckCreateOnPremiseErrorComponent
                | ApiV1WorkspacesCheckCreateOrganizationIdErrorComponent
                | ApiV1WorkspacesCheckCreateOwnerIdErrorComponent
                | ApiV1WorkspacesCheckCreatePlatformServiceErrorComponent
                | ApiV1WorkspacesCheckCreatePopIdErrorComponent
                | ApiV1WorkspacesCheckCreateProviderErrorComponent
                | ApiV1WorkspacesCheckCreateProviderIdErrorComponent
                | ApiV1WorkspacesCheckCreateProviderReferenceErrorComponent
                | ApiV1WorkspacesCheckCreatePurposeErrorComponent
                | ApiV1WorkspacesCheckCreateReadmeMdErrorComponent
                | ApiV1WorkspacesCheckCreateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesCheckCreateScopeErrorComponent
                | ApiV1WorkspacesCheckCreateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesCheckCreateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesCheckCreateSlaTargetErrorComponent
                | ApiV1WorkspacesCheckCreateSloAvailabilityErrorComponent
                | ApiV1WorkspacesCheckCreateSloTargetErrorComponent
                | ApiV1WorkspacesCheckCreateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesCheckCreateTemplateErrorComponent
                | ApiV1WorkspacesCheckCreateUrlsErrorComponent
                | ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_0 = (
                        ApiV1WorkspacesCheckCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_1 = (
                        ApiV1WorkspacesCheckCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_2 = (
                        ApiV1WorkspacesCheckCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_3 = (
                        ApiV1WorkspacesCheckCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_4 = (
                        ApiV1WorkspacesCheckCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_5 = (
                        ApiV1WorkspacesCheckCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_6 = (
                        ApiV1WorkspacesCheckCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_7 = (
                        ApiV1WorkspacesCheckCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_8 = (
                        ApiV1WorkspacesCheckCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_9 = (
                        ApiV1WorkspacesCheckCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_10 = (
                        ApiV1WorkspacesCheckCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_11 = (
                        ApiV1WorkspacesCheckCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_12 = (
                        ApiV1WorkspacesCheckCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_13 = (
                        ApiV1WorkspacesCheckCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_14 = (
                        ApiV1WorkspacesCheckCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_15 = (
                        ApiV1WorkspacesCheckCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_16 = (
                        ApiV1WorkspacesCheckCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_17 = (
                        ApiV1WorkspacesCheckCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_18 = (
                        ApiV1WorkspacesCheckCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_19 = (
                        ApiV1WorkspacesCheckCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_20 = (
                        ApiV1WorkspacesCheckCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_21 = (
                        ApiV1WorkspacesCheckCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_22 = (
                        ApiV1WorkspacesCheckCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_23 = (
                        ApiV1WorkspacesCheckCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_24 = (
                        ApiV1WorkspacesCheckCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_25 = (
                        ApiV1WorkspacesCheckCreateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_26 = (
                        ApiV1WorkspacesCheckCreateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_27 = (
                        ApiV1WorkspacesCheckCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_28 = (
                        ApiV1WorkspacesCheckCreateGlobalEndpointMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_29 = (
                        ApiV1WorkspacesCheckCreateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_30 = (
                        ApiV1WorkspacesCheckCreateNotificationsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_31 = (
                        ApiV1WorkspacesCheckCreateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_32 = (
                        ApiV1WorkspacesCheckCreateHasIncompatibleKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_33 = (
                        ApiV1WorkspacesCheckCreateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_34 = (
                        ApiV1WorkspacesCheckCreateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_35 = (
                        ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_36 = (
                        ApiV1WorkspacesCheckCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_37 = (
                        ApiV1WorkspacesCheckCreateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_38 = (
                        ApiV1WorkspacesCheckCreatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_39 = (
                        ApiV1WorkspacesCheckCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_40 = (
                        ApiV1WorkspacesCheckCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_41 = (
                        ApiV1WorkspacesCheckCreatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_42 = (
                        ApiV1WorkspacesCheckCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_43 = (
                        ApiV1WorkspacesCheckCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_check_create_error_type_44 = (
                        ApiV1WorkspacesCheckCreateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_check_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_check_create_error_type_45 = (
                    ApiV1WorkspacesCheckCreateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_check_create_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_check_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_check_create_validation_error.additional_properties = d
        return api_v1_workspaces_check_create_validation_error

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
