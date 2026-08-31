from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_discover_create_actual_availability_error_component import (
        ApiV1WorkspacesDiscoverCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_alternative_name_error_component import (
        ApiV1WorkspacesDiscoverCreateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_annotations_error_component import (
        ApiV1WorkspacesDiscoverCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_archived_at_error_component import (
        ApiV1WorkspacesDiscoverCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_archived_error_component import (
        ApiV1WorkspacesDiscoverCreateArchivedErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_archived_reason_error_component import (
        ApiV1WorkspacesDiscoverCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_backup_enabled_error_component import (
        ApiV1WorkspacesDiscoverCreateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_criticality_error_component import (
        ApiV1WorkspacesDiscoverCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_debug_mode_error_component import (
        ApiV1WorkspacesDiscoverCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_description_error_component import (
        ApiV1WorkspacesDiscoverCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_discovery_enabled_error_component import (
        ApiV1WorkspacesDiscoverCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_display_name_error_component import (
        ApiV1WorkspacesDiscoverCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_encrypted_error_component import (
        ApiV1WorkspacesDiscoverCreateEncryptedErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesDiscoverCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_endpoint_monitors_error_component import (
        ApiV1WorkspacesDiscoverCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_gitlab_project_id_error_component import (
        ApiV1WorkspacesDiscoverCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_gitlab_project_url_error_component import (
        ApiV1WorkspacesDiscoverCreateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesDiscoverCreateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesDiscoverCreateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_kind_error_component import (
        ApiV1WorkspacesDiscoverCreateKindErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_labels_error_component import (
        ApiV1WorkspacesDiscoverCreateLabelsErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesDiscoverCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_name_error_component import (
        ApiV1WorkspacesDiscoverCreateNameErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_non_field_errors_error_component import (
        ApiV1WorkspacesDiscoverCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_notifications_enabled_error_component import (
        ApiV1WorkspacesDiscoverCreateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_on_premise_error_component import (
        ApiV1WorkspacesDiscoverCreateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_organization_id_error_component import (
        ApiV1WorkspacesDiscoverCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_owner_id_error_component import (
        ApiV1WorkspacesDiscoverCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_platform_service_error_component import (
        ApiV1WorkspacesDiscoverCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_pop_id_error_component import (
        ApiV1WorkspacesDiscoverCreatePopIdErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_provider_error_component import (
        ApiV1WorkspacesDiscoverCreateProviderErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_provider_id_error_component import (
        ApiV1WorkspacesDiscoverCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_provider_reference_error_component import (
        ApiV1WorkspacesDiscoverCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_purpose_error_component import (
        ApiV1WorkspacesDiscoverCreatePurposeErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_readme_md_error_component import (
        ApiV1WorkspacesDiscoverCreateReadmeMdErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_reconciliation_enabled_error_component import (
        ApiV1WorkspacesDiscoverCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_scope_error_component import (
        ApiV1WorkspacesDiscoverCreateScopeErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_secrets_poly_raw_error_component import (
        ApiV1WorkspacesDiscoverCreateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_sla_availability_error_component import (
        ApiV1WorkspacesDiscoverCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_sla_target_error_component import (
        ApiV1WorkspacesDiscoverCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_slo_availability_error_component import (
        ApiV1WorkspacesDiscoverCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_slo_target_error_component import (
        ApiV1WorkspacesDiscoverCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_target_availability_error_component import (
        ApiV1WorkspacesDiscoverCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_template_error_component import (
        ApiV1WorkspacesDiscoverCreateTemplateErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_urls_error_component import (
        ApiV1WorkspacesDiscoverCreateUrlsErrorComponent,
    )
    from ..models.api_v1_workspaces_discover_create_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesDiscoverCreateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesDiscoverCreateValidationError")


@_attrs_define
class ApiV1WorkspacesDiscoverCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesDiscoverCreateActualAvailabilityErrorComponent |
            ApiV1WorkspacesDiscoverCreateAlternativeNameErrorComponent |
            ApiV1WorkspacesDiscoverCreateAnnotationsErrorComponent | ApiV1WorkspacesDiscoverCreateArchivedAtErrorComponent |
            ApiV1WorkspacesDiscoverCreateArchivedErrorComponent | ApiV1WorkspacesDiscoverCreateArchivedReasonErrorComponent
            | ApiV1WorkspacesDiscoverCreateBackupEnabledErrorComponent |
            ApiV1WorkspacesDiscoverCreateCriticalityErrorComponent | ApiV1WorkspacesDiscoverCreateDebugModeErrorComponent |
            ApiV1WorkspacesDiscoverCreateDescriptionErrorComponent |
            ApiV1WorkspacesDiscoverCreateDiscoveryEnabledErrorComponent |
            ApiV1WorkspacesDiscoverCreateDisplayNameErrorComponent | ApiV1WorkspacesDiscoverCreateEncryptedErrorComponent |
            ApiV1WorkspacesDiscoverCreateEndpointMonitoringModeErrorComponent |
            ApiV1WorkspacesDiscoverCreateEndpointMonitorsErrorComponent |
            ApiV1WorkspacesDiscoverCreateGitlabProjectIdErrorComponent |
            ApiV1WorkspacesDiscoverCreateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesDiscoverCreateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesDiscoverCreateHasIncompatibleKubeconfigErrorComponent |
            ApiV1WorkspacesDiscoverCreateKindErrorComponent | ApiV1WorkspacesDiscoverCreateLabelsErrorComponent |
            ApiV1WorkspacesDiscoverCreateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesDiscoverCreateNameErrorComponent | ApiV1WorkspacesDiscoverCreateNonFieldErrorsErrorComponent |
            ApiV1WorkspacesDiscoverCreateNotificationsEnabledErrorComponent |
            ApiV1WorkspacesDiscoverCreateOnPremiseErrorComponent | ApiV1WorkspacesDiscoverCreateOrganizationIdErrorComponent
            | ApiV1WorkspacesDiscoverCreateOwnerIdErrorComponent |
            ApiV1WorkspacesDiscoverCreatePlatformServiceErrorComponent | ApiV1WorkspacesDiscoverCreatePopIdErrorComponent |
            ApiV1WorkspacesDiscoverCreateProviderErrorComponent | ApiV1WorkspacesDiscoverCreateProviderIdErrorComponent |
            ApiV1WorkspacesDiscoverCreateProviderReferenceErrorComponent |
            ApiV1WorkspacesDiscoverCreatePurposeErrorComponent | ApiV1WorkspacesDiscoverCreateReadmeMdErrorComponent |
            ApiV1WorkspacesDiscoverCreateReconciliationEnabledErrorComponent |
            ApiV1WorkspacesDiscoverCreateScopeErrorComponent | ApiV1WorkspacesDiscoverCreateSecretsPolyRawErrorComponent |
            ApiV1WorkspacesDiscoverCreateSlaAvailabilityErrorComponent |
            ApiV1WorkspacesDiscoverCreateSlaTargetErrorComponent |
            ApiV1WorkspacesDiscoverCreateSloAvailabilityErrorComponent |
            ApiV1WorkspacesDiscoverCreateSloTargetErrorComponent |
            ApiV1WorkspacesDiscoverCreateTargetAvailabilityErrorComponent |
            ApiV1WorkspacesDiscoverCreateTemplateErrorComponent | ApiV1WorkspacesDiscoverCreateUrlsErrorComponent |
            ApiV1WorkspacesDiscoverCreateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesDiscoverCreateActualAvailabilityErrorComponent
        | ApiV1WorkspacesDiscoverCreateAlternativeNameErrorComponent
        | ApiV1WorkspacesDiscoverCreateAnnotationsErrorComponent
        | ApiV1WorkspacesDiscoverCreateArchivedAtErrorComponent
        | ApiV1WorkspacesDiscoverCreateArchivedErrorComponent
        | ApiV1WorkspacesDiscoverCreateArchivedReasonErrorComponent
        | ApiV1WorkspacesDiscoverCreateBackupEnabledErrorComponent
        | ApiV1WorkspacesDiscoverCreateCriticalityErrorComponent
        | ApiV1WorkspacesDiscoverCreateDebugModeErrorComponent
        | ApiV1WorkspacesDiscoverCreateDescriptionErrorComponent
        | ApiV1WorkspacesDiscoverCreateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesDiscoverCreateDisplayNameErrorComponent
        | ApiV1WorkspacesDiscoverCreateEncryptedErrorComponent
        | ApiV1WorkspacesDiscoverCreateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesDiscoverCreateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesDiscoverCreateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesDiscoverCreateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesDiscoverCreateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesDiscoverCreateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesDiscoverCreateKindErrorComponent
        | ApiV1WorkspacesDiscoverCreateLabelsErrorComponent
        | ApiV1WorkspacesDiscoverCreateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesDiscoverCreateNameErrorComponent
        | ApiV1WorkspacesDiscoverCreateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesDiscoverCreateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesDiscoverCreateOnPremiseErrorComponent
        | ApiV1WorkspacesDiscoverCreateOrganizationIdErrorComponent
        | ApiV1WorkspacesDiscoverCreateOwnerIdErrorComponent
        | ApiV1WorkspacesDiscoverCreatePlatformServiceErrorComponent
        | ApiV1WorkspacesDiscoverCreatePopIdErrorComponent
        | ApiV1WorkspacesDiscoverCreateProviderErrorComponent
        | ApiV1WorkspacesDiscoverCreateProviderIdErrorComponent
        | ApiV1WorkspacesDiscoverCreateProviderReferenceErrorComponent
        | ApiV1WorkspacesDiscoverCreatePurposeErrorComponent
        | ApiV1WorkspacesDiscoverCreateReadmeMdErrorComponent
        | ApiV1WorkspacesDiscoverCreateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesDiscoverCreateScopeErrorComponent
        | ApiV1WorkspacesDiscoverCreateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesDiscoverCreateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesDiscoverCreateSlaTargetErrorComponent
        | ApiV1WorkspacesDiscoverCreateSloAvailabilityErrorComponent
        | ApiV1WorkspacesDiscoverCreateSloTargetErrorComponent
        | ApiV1WorkspacesDiscoverCreateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesDiscoverCreateTemplateErrorComponent
        | ApiV1WorkspacesDiscoverCreateUrlsErrorComponent
        | ApiV1WorkspacesDiscoverCreateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_discover_create_actual_availability_error_component import (
            ApiV1WorkspacesDiscoverCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_annotations_error_component import (
            ApiV1WorkspacesDiscoverCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_archived_at_error_component import (
            ApiV1WorkspacesDiscoverCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_archived_error_component import (
            ApiV1WorkspacesDiscoverCreateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_archived_reason_error_component import (
            ApiV1WorkspacesDiscoverCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_backup_enabled_error_component import (
            ApiV1WorkspacesDiscoverCreateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_criticality_error_component import (
            ApiV1WorkspacesDiscoverCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_debug_mode_error_component import (
            ApiV1WorkspacesDiscoverCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_description_error_component import (
            ApiV1WorkspacesDiscoverCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_discovery_enabled_error_component import (
            ApiV1WorkspacesDiscoverCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_display_name_error_component import (
            ApiV1WorkspacesDiscoverCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_encrypted_error_component import (
            ApiV1WorkspacesDiscoverCreateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesDiscoverCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesDiscoverCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesDiscoverCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesDiscoverCreateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesDiscoverCreateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesDiscoverCreateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_kind_error_component import (
            ApiV1WorkspacesDiscoverCreateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_labels_error_component import (
            ApiV1WorkspacesDiscoverCreateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesDiscoverCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_name_error_component import (
            ApiV1WorkspacesDiscoverCreateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_non_field_errors_error_component import (
            ApiV1WorkspacesDiscoverCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_notifications_enabled_error_component import (
            ApiV1WorkspacesDiscoverCreateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_on_premise_error_component import (
            ApiV1WorkspacesDiscoverCreateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_organization_id_error_component import (
            ApiV1WorkspacesDiscoverCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_owner_id_error_component import (
            ApiV1WorkspacesDiscoverCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_platform_service_error_component import (
            ApiV1WorkspacesDiscoverCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_pop_id_error_component import (
            ApiV1WorkspacesDiscoverCreatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_provider_error_component import (
            ApiV1WorkspacesDiscoverCreateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_provider_id_error_component import (
            ApiV1WorkspacesDiscoverCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_provider_reference_error_component import (
            ApiV1WorkspacesDiscoverCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_purpose_error_component import (
            ApiV1WorkspacesDiscoverCreatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_readme_md_error_component import (
            ApiV1WorkspacesDiscoverCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesDiscoverCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_scope_error_component import (
            ApiV1WorkspacesDiscoverCreateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesDiscoverCreateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_sla_availability_error_component import (
            ApiV1WorkspacesDiscoverCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_sla_target_error_component import (
            ApiV1WorkspacesDiscoverCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_slo_availability_error_component import (
            ApiV1WorkspacesDiscoverCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_slo_target_error_component import (
            ApiV1WorkspacesDiscoverCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_target_availability_error_component import (
            ApiV1WorkspacesDiscoverCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_template_error_component import (
            ApiV1WorkspacesDiscoverCreateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_urls_error_component import (
            ApiV1WorkspacesDiscoverCreateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesDiscoverCreateWorkspaceInventoryRawErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateGitlabProjectUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateGlobalEndpointMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesDiscoverCreateMonitoringWorkspaceAllowlistIdsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateNotificationsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateBackupEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateHasIncompatibleKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateEndpointMonitorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateSecretsPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateWorkspaceInventoryRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesDiscoverCreateReadmeMdErrorComponent):
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
        from ..models.api_v1_workspaces_discover_create_actual_availability_error_component import (
            ApiV1WorkspacesDiscoverCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_alternative_name_error_component import (
            ApiV1WorkspacesDiscoverCreateAlternativeNameErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_annotations_error_component import (
            ApiV1WorkspacesDiscoverCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_archived_at_error_component import (
            ApiV1WorkspacesDiscoverCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_archived_error_component import (
            ApiV1WorkspacesDiscoverCreateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_archived_reason_error_component import (
            ApiV1WorkspacesDiscoverCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_backup_enabled_error_component import (
            ApiV1WorkspacesDiscoverCreateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_criticality_error_component import (
            ApiV1WorkspacesDiscoverCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_debug_mode_error_component import (
            ApiV1WorkspacesDiscoverCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_description_error_component import (
            ApiV1WorkspacesDiscoverCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_discovery_enabled_error_component import (
            ApiV1WorkspacesDiscoverCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_display_name_error_component import (
            ApiV1WorkspacesDiscoverCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_encrypted_error_component import (
            ApiV1WorkspacesDiscoverCreateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesDiscoverCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesDiscoverCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesDiscoverCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesDiscoverCreateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesDiscoverCreateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesDiscoverCreateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_kind_error_component import (
            ApiV1WorkspacesDiscoverCreateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_labels_error_component import (
            ApiV1WorkspacesDiscoverCreateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesDiscoverCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_name_error_component import (
            ApiV1WorkspacesDiscoverCreateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_non_field_errors_error_component import (
            ApiV1WorkspacesDiscoverCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_notifications_enabled_error_component import (
            ApiV1WorkspacesDiscoverCreateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_on_premise_error_component import (
            ApiV1WorkspacesDiscoverCreateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_organization_id_error_component import (
            ApiV1WorkspacesDiscoverCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_owner_id_error_component import (
            ApiV1WorkspacesDiscoverCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_platform_service_error_component import (
            ApiV1WorkspacesDiscoverCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_pop_id_error_component import (
            ApiV1WorkspacesDiscoverCreatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_provider_error_component import (
            ApiV1WorkspacesDiscoverCreateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_provider_id_error_component import (
            ApiV1WorkspacesDiscoverCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_provider_reference_error_component import (
            ApiV1WorkspacesDiscoverCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_purpose_error_component import (
            ApiV1WorkspacesDiscoverCreatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_readme_md_error_component import (
            ApiV1WorkspacesDiscoverCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesDiscoverCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_scope_error_component import (
            ApiV1WorkspacesDiscoverCreateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesDiscoverCreateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_sla_availability_error_component import (
            ApiV1WorkspacesDiscoverCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_sla_target_error_component import (
            ApiV1WorkspacesDiscoverCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_slo_availability_error_component import (
            ApiV1WorkspacesDiscoverCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_slo_target_error_component import (
            ApiV1WorkspacesDiscoverCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_target_availability_error_component import (
            ApiV1WorkspacesDiscoverCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_template_error_component import (
            ApiV1WorkspacesDiscoverCreateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_urls_error_component import (
            ApiV1WorkspacesDiscoverCreateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_discover_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesDiscoverCreateWorkspaceInventoryRawErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesDiscoverCreateActualAvailabilityErrorComponent
                | ApiV1WorkspacesDiscoverCreateAlternativeNameErrorComponent
                | ApiV1WorkspacesDiscoverCreateAnnotationsErrorComponent
                | ApiV1WorkspacesDiscoverCreateArchivedAtErrorComponent
                | ApiV1WorkspacesDiscoverCreateArchivedErrorComponent
                | ApiV1WorkspacesDiscoverCreateArchivedReasonErrorComponent
                | ApiV1WorkspacesDiscoverCreateBackupEnabledErrorComponent
                | ApiV1WorkspacesDiscoverCreateCriticalityErrorComponent
                | ApiV1WorkspacesDiscoverCreateDebugModeErrorComponent
                | ApiV1WorkspacesDiscoverCreateDescriptionErrorComponent
                | ApiV1WorkspacesDiscoverCreateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesDiscoverCreateDisplayNameErrorComponent
                | ApiV1WorkspacesDiscoverCreateEncryptedErrorComponent
                | ApiV1WorkspacesDiscoverCreateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesDiscoverCreateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesDiscoverCreateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesDiscoverCreateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesDiscoverCreateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesDiscoverCreateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesDiscoverCreateKindErrorComponent
                | ApiV1WorkspacesDiscoverCreateLabelsErrorComponent
                | ApiV1WorkspacesDiscoverCreateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesDiscoverCreateNameErrorComponent
                | ApiV1WorkspacesDiscoverCreateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesDiscoverCreateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesDiscoverCreateOnPremiseErrorComponent
                | ApiV1WorkspacesDiscoverCreateOrganizationIdErrorComponent
                | ApiV1WorkspacesDiscoverCreateOwnerIdErrorComponent
                | ApiV1WorkspacesDiscoverCreatePlatformServiceErrorComponent
                | ApiV1WorkspacesDiscoverCreatePopIdErrorComponent
                | ApiV1WorkspacesDiscoverCreateProviderErrorComponent
                | ApiV1WorkspacesDiscoverCreateProviderIdErrorComponent
                | ApiV1WorkspacesDiscoverCreateProviderReferenceErrorComponent
                | ApiV1WorkspacesDiscoverCreatePurposeErrorComponent
                | ApiV1WorkspacesDiscoverCreateReadmeMdErrorComponent
                | ApiV1WorkspacesDiscoverCreateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesDiscoverCreateScopeErrorComponent
                | ApiV1WorkspacesDiscoverCreateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesDiscoverCreateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesDiscoverCreateSlaTargetErrorComponent
                | ApiV1WorkspacesDiscoverCreateSloAvailabilityErrorComponent
                | ApiV1WorkspacesDiscoverCreateSloTargetErrorComponent
                | ApiV1WorkspacesDiscoverCreateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesDiscoverCreateTemplateErrorComponent
                | ApiV1WorkspacesDiscoverCreateUrlsErrorComponent
                | ApiV1WorkspacesDiscoverCreateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_0 = (
                        ApiV1WorkspacesDiscoverCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_1 = (
                        ApiV1WorkspacesDiscoverCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_2 = (
                        ApiV1WorkspacesDiscoverCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_3 = (
                        ApiV1WorkspacesDiscoverCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_4 = (
                        ApiV1WorkspacesDiscoverCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_5 = (
                        ApiV1WorkspacesDiscoverCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_6 = (
                        ApiV1WorkspacesDiscoverCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_7 = (
                        ApiV1WorkspacesDiscoverCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_8 = (
                        ApiV1WorkspacesDiscoverCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_9 = (
                        ApiV1WorkspacesDiscoverCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_10 = (
                        ApiV1WorkspacesDiscoverCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_11 = (
                        ApiV1WorkspacesDiscoverCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_12 = (
                        ApiV1WorkspacesDiscoverCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_13 = (
                        ApiV1WorkspacesDiscoverCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_14 = (
                        ApiV1WorkspacesDiscoverCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_15 = (
                        ApiV1WorkspacesDiscoverCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_16 = (
                        ApiV1WorkspacesDiscoverCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_17 = (
                        ApiV1WorkspacesDiscoverCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_18 = (
                        ApiV1WorkspacesDiscoverCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_19 = (
                        ApiV1WorkspacesDiscoverCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_20 = (
                        ApiV1WorkspacesDiscoverCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_21 = (
                        ApiV1WorkspacesDiscoverCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_22 = (
                        ApiV1WorkspacesDiscoverCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_23 = (
                        ApiV1WorkspacesDiscoverCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_24 = (
                        ApiV1WorkspacesDiscoverCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_25 = (
                        ApiV1WorkspacesDiscoverCreateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_26 = (
                        ApiV1WorkspacesDiscoverCreateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_27 = (
                        ApiV1WorkspacesDiscoverCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_28 = (
                        ApiV1WorkspacesDiscoverCreateGlobalEndpointMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_29 = (
                        ApiV1WorkspacesDiscoverCreateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_30 = (
                        ApiV1WorkspacesDiscoverCreateNotificationsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_31 = (
                        ApiV1WorkspacesDiscoverCreateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_32 = (
                        ApiV1WorkspacesDiscoverCreateHasIncompatibleKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_33 = (
                        ApiV1WorkspacesDiscoverCreateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_34 = (
                        ApiV1WorkspacesDiscoverCreateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_35 = (
                        ApiV1WorkspacesDiscoverCreateWorkspaceInventoryRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_36 = (
                        ApiV1WorkspacesDiscoverCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_37 = (
                        ApiV1WorkspacesDiscoverCreateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_38 = (
                        ApiV1WorkspacesDiscoverCreatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_39 = (
                        ApiV1WorkspacesDiscoverCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_40 = (
                        ApiV1WorkspacesDiscoverCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_41 = (
                        ApiV1WorkspacesDiscoverCreatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_42 = (
                        ApiV1WorkspacesDiscoverCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_43 = (
                        ApiV1WorkspacesDiscoverCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_discover_create_error_type_44 = (
                        ApiV1WorkspacesDiscoverCreateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_discover_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_discover_create_error_type_45 = (
                    ApiV1WorkspacesDiscoverCreateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_discover_create_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_discover_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_discover_create_validation_error.additional_properties = d
        return api_v1_workspaces_discover_create_validation_error

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
