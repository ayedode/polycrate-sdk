from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_update_actual_availability_error_component import (
        ApiV1WorkspacesUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_alternative_name_error_component import (
        ApiV1WorkspacesUpdateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_update_annotations_error_component import (
        ApiV1WorkspacesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_archived_at_error_component import (
        ApiV1WorkspacesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_update_archived_error_component import ApiV1WorkspacesUpdateArchivedErrorComponent
    from ..models.api_v1_workspaces_update_archived_reason_error_component import (
        ApiV1WorkspacesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_update_backup_enabled_error_component import (
        ApiV1WorkspacesUpdateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_update_criticality_error_component import (
        ApiV1WorkspacesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_debug_mode_error_component import (
        ApiV1WorkspacesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_update_description_error_component import (
        ApiV1WorkspacesUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_update_discovery_enabled_error_component import (
        ApiV1WorkspacesUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_update_display_name_error_component import (
        ApiV1WorkspacesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_update_encrypted_error_component import ApiV1WorkspacesUpdateEncryptedErrorComponent
    from ..models.api_v1_workspaces_update_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesUpdateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_update_endpoint_monitors_error_component import (
        ApiV1WorkspacesUpdateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_gitlab_project_id_error_component import (
        ApiV1WorkspacesUpdateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_gitlab_project_url_error_component import (
        ApiV1WorkspacesUpdateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_update_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesUpdateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_update_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesUpdateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_update_kind_error_component import ApiV1WorkspacesUpdateKindErrorComponent
    from ..models.api_v1_workspaces_update_labels_error_component import ApiV1WorkspacesUpdateLabelsErrorComponent
    from ..models.api_v1_workspaces_update_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_name_error_component import ApiV1WorkspacesUpdateNameErrorComponent
    from ..models.api_v1_workspaces_update_non_field_errors_error_component import (
        ApiV1WorkspacesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_notifications_enabled_error_component import (
        ApiV1WorkspacesUpdateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_update_on_premise_error_component import (
        ApiV1WorkspacesUpdateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_update_organization_id_error_component import (
        ApiV1WorkspacesUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_owner_id_error_component import ApiV1WorkspacesUpdateOwnerIdErrorComponent
    from ..models.api_v1_workspaces_update_platform_service_error_component import (
        ApiV1WorkspacesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_update_pop_id_error_component import ApiV1WorkspacesUpdatePopIdErrorComponent
    from ..models.api_v1_workspaces_update_provider_error_component import ApiV1WorkspacesUpdateProviderErrorComponent
    from ..models.api_v1_workspaces_update_provider_id_error_component import (
        ApiV1WorkspacesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_provider_reference_error_component import (
        ApiV1WorkspacesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_update_purpose_error_component import ApiV1WorkspacesUpdatePurposeErrorComponent
    from ..models.api_v1_workspaces_update_readme_md_error_component import ApiV1WorkspacesUpdateReadmeMdErrorComponent
    from ..models.api_v1_workspaces_update_reconciliation_enabled_error_component import (
        ApiV1WorkspacesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_update_scope_error_component import ApiV1WorkspacesUpdateScopeErrorComponent
    from ..models.api_v1_workspaces_update_secrets_poly_raw_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_update_sla_availability_error_component import (
        ApiV1WorkspacesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_sla_target_error_component import (
        ApiV1WorkspacesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_update_slo_availability_error_component import (
        ApiV1WorkspacesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_slo_target_error_component import (
        ApiV1WorkspacesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_update_target_availability_error_component import (
        ApiV1WorkspacesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_template_error_component import ApiV1WorkspacesUpdateTemplateErrorComponent
    from ..models.api_v1_workspaces_update_urls_error_component import ApiV1WorkspacesUpdateUrlsErrorComponent
    from ..models.api_v1_workspaces_update_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesUpdateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesUpdateValidationError")


@_attrs_define
class ApiV1WorkspacesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesUpdateActualAvailabilityErrorComponent |
            ApiV1WorkspacesUpdateAlternativeNameErrorComponent | ApiV1WorkspacesUpdateAnnotationsErrorComponent |
            ApiV1WorkspacesUpdateArchivedAtErrorComponent | ApiV1WorkspacesUpdateArchivedErrorComponent |
            ApiV1WorkspacesUpdateArchivedReasonErrorComponent | ApiV1WorkspacesUpdateBackupEnabledErrorComponent |
            ApiV1WorkspacesUpdateCriticalityErrorComponent | ApiV1WorkspacesUpdateDebugModeErrorComponent |
            ApiV1WorkspacesUpdateDescriptionErrorComponent | ApiV1WorkspacesUpdateDiscoveryEnabledErrorComponent |
            ApiV1WorkspacesUpdateDisplayNameErrorComponent | ApiV1WorkspacesUpdateEncryptedErrorComponent |
            ApiV1WorkspacesUpdateEndpointMonitoringModeErrorComponent | ApiV1WorkspacesUpdateEndpointMonitorsErrorComponent
            | ApiV1WorkspacesUpdateGitlabProjectIdErrorComponent | ApiV1WorkspacesUpdateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesUpdateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesUpdateHasIncompatibleKubeconfigErrorComponent | ApiV1WorkspacesUpdateKindErrorComponent |
            ApiV1WorkspacesUpdateLabelsErrorComponent | ApiV1WorkspacesUpdateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesUpdateNameErrorComponent | ApiV1WorkspacesUpdateNonFieldErrorsErrorComponent |
            ApiV1WorkspacesUpdateNotificationsEnabledErrorComponent | ApiV1WorkspacesUpdateOnPremiseErrorComponent |
            ApiV1WorkspacesUpdateOrganizationIdErrorComponent | ApiV1WorkspacesUpdateOwnerIdErrorComponent |
            ApiV1WorkspacesUpdatePlatformServiceErrorComponent | ApiV1WorkspacesUpdatePopIdErrorComponent |
            ApiV1WorkspacesUpdateProviderErrorComponent | ApiV1WorkspacesUpdateProviderIdErrorComponent |
            ApiV1WorkspacesUpdateProviderReferenceErrorComponent | ApiV1WorkspacesUpdatePurposeErrorComponent |
            ApiV1WorkspacesUpdateReadmeMdErrorComponent | ApiV1WorkspacesUpdateReconciliationEnabledErrorComponent |
            ApiV1WorkspacesUpdateScopeErrorComponent | ApiV1WorkspacesUpdateSecretsPolyRawErrorComponent |
            ApiV1WorkspacesUpdateSlaAvailabilityErrorComponent | ApiV1WorkspacesUpdateSlaTargetErrorComponent |
            ApiV1WorkspacesUpdateSloAvailabilityErrorComponent | ApiV1WorkspacesUpdateSloTargetErrorComponent |
            ApiV1WorkspacesUpdateTargetAvailabilityErrorComponent | ApiV1WorkspacesUpdateTemplateErrorComponent |
            ApiV1WorkspacesUpdateUrlsErrorComponent | ApiV1WorkspacesUpdateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesUpdateActualAvailabilityErrorComponent
        | ApiV1WorkspacesUpdateAlternativeNameErrorComponent
        | ApiV1WorkspacesUpdateAnnotationsErrorComponent
        | ApiV1WorkspacesUpdateArchivedAtErrorComponent
        | ApiV1WorkspacesUpdateArchivedErrorComponent
        | ApiV1WorkspacesUpdateArchivedReasonErrorComponent
        | ApiV1WorkspacesUpdateBackupEnabledErrorComponent
        | ApiV1WorkspacesUpdateCriticalityErrorComponent
        | ApiV1WorkspacesUpdateDebugModeErrorComponent
        | ApiV1WorkspacesUpdateDescriptionErrorComponent
        | ApiV1WorkspacesUpdateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesUpdateDisplayNameErrorComponent
        | ApiV1WorkspacesUpdateEncryptedErrorComponent
        | ApiV1WorkspacesUpdateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesUpdateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesUpdateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesUpdateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesUpdateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesUpdateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesUpdateKindErrorComponent
        | ApiV1WorkspacesUpdateLabelsErrorComponent
        | ApiV1WorkspacesUpdateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesUpdateNameErrorComponent
        | ApiV1WorkspacesUpdateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesUpdateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesUpdateOnPremiseErrorComponent
        | ApiV1WorkspacesUpdateOrganizationIdErrorComponent
        | ApiV1WorkspacesUpdateOwnerIdErrorComponent
        | ApiV1WorkspacesUpdatePlatformServiceErrorComponent
        | ApiV1WorkspacesUpdatePopIdErrorComponent
        | ApiV1WorkspacesUpdateProviderErrorComponent
        | ApiV1WorkspacesUpdateProviderIdErrorComponent
        | ApiV1WorkspacesUpdateProviderReferenceErrorComponent
        | ApiV1WorkspacesUpdatePurposeErrorComponent
        | ApiV1WorkspacesUpdateReadmeMdErrorComponent
        | ApiV1WorkspacesUpdateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesUpdateScopeErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesUpdateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesUpdateSlaTargetErrorComponent
        | ApiV1WorkspacesUpdateSloAvailabilityErrorComponent
        | ApiV1WorkspacesUpdateSloTargetErrorComponent
        | ApiV1WorkspacesUpdateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesUpdateTemplateErrorComponent
        | ApiV1WorkspacesUpdateUrlsErrorComponent
        | ApiV1WorkspacesUpdateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_update_actual_availability_error_component import (
            ApiV1WorkspacesUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_annotations_error_component import (
            ApiV1WorkspacesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_archived_at_error_component import (
            ApiV1WorkspacesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_update_archived_error_component import (
            ApiV1WorkspacesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_update_archived_reason_error_component import (
            ApiV1WorkspacesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_update_backup_enabled_error_component import (
            ApiV1WorkspacesUpdateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_criticality_error_component import (
            ApiV1WorkspacesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_debug_mode_error_component import (
            ApiV1WorkspacesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_description_error_component import (
            ApiV1WorkspacesUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_update_discovery_enabled_error_component import (
            ApiV1WorkspacesUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_display_name_error_component import (
            ApiV1WorkspacesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_encrypted_error_component import (
            ApiV1WorkspacesUpdateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_update_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesUpdateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_endpoint_monitors_error_component import (
            ApiV1WorkspacesUpdateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_gitlab_project_id_error_component import (
            ApiV1WorkspacesUpdateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_gitlab_project_url_error_component import (
            ApiV1WorkspacesUpdateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_update_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesUpdateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_update_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesUpdateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_update_kind_error_component import ApiV1WorkspacesUpdateKindErrorComponent
        from ..models.api_v1_workspaces_update_labels_error_component import ApiV1WorkspacesUpdateLabelsErrorComponent
        from ..models.api_v1_workspaces_update_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_name_error_component import ApiV1WorkspacesUpdateNameErrorComponent
        from ..models.api_v1_workspaces_update_non_field_errors_error_component import (
            ApiV1WorkspacesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_notifications_enabled_error_component import (
            ApiV1WorkspacesUpdateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_on_premise_error_component import (
            ApiV1WorkspacesUpdateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_update_organization_id_error_component import (
            ApiV1WorkspacesUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_owner_id_error_component import (
            ApiV1WorkspacesUpdateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_platform_service_error_component import (
            ApiV1WorkspacesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_update_pop_id_error_component import ApiV1WorkspacesUpdatePopIdErrorComponent
        from ..models.api_v1_workspaces_update_provider_error_component import (
            ApiV1WorkspacesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_update_provider_id_error_component import (
            ApiV1WorkspacesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_provider_reference_error_component import (
            ApiV1WorkspacesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_update_purpose_error_component import ApiV1WorkspacesUpdatePurposeErrorComponent
        from ..models.api_v1_workspaces_update_readme_md_error_component import (
            ApiV1WorkspacesUpdateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_reconciliation_enabled_error_component import (
            ApiV1WorkspacesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_scope_error_component import ApiV1WorkspacesUpdateScopeErrorComponent
        from ..models.api_v1_workspaces_update_secrets_poly_raw_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_update_sla_availability_error_component import (
            ApiV1WorkspacesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_sla_target_error_component import (
            ApiV1WorkspacesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_update_slo_availability_error_component import (
            ApiV1WorkspacesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_slo_target_error_component import (
            ApiV1WorkspacesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_update_target_availability_error_component import (
            ApiV1WorkspacesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_template_error_component import (
            ApiV1WorkspacesUpdateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_update_urls_error_component import ApiV1WorkspacesUpdateUrlsErrorComponent
        from ..models.api_v1_workspaces_update_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesUpdateWorkspaceInventoryRawErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateGitlabProjectUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateGlobalEndpointMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateMonitoringWorkspaceAllowlistIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateNotificationsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateBackupEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateHasIncompatibleKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateEndpointMonitorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspaceInventoryRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateReadmeMdErrorComponent):
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
        from ..models.api_v1_workspaces_update_actual_availability_error_component import (
            ApiV1WorkspacesUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_alternative_name_error_component import (
            ApiV1WorkspacesUpdateAlternativeNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_annotations_error_component import (
            ApiV1WorkspacesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_archived_at_error_component import (
            ApiV1WorkspacesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_update_archived_error_component import (
            ApiV1WorkspacesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_update_archived_reason_error_component import (
            ApiV1WorkspacesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_update_backup_enabled_error_component import (
            ApiV1WorkspacesUpdateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_criticality_error_component import (
            ApiV1WorkspacesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_debug_mode_error_component import (
            ApiV1WorkspacesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_description_error_component import (
            ApiV1WorkspacesUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_update_discovery_enabled_error_component import (
            ApiV1WorkspacesUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_display_name_error_component import (
            ApiV1WorkspacesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_encrypted_error_component import (
            ApiV1WorkspacesUpdateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_update_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesUpdateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_endpoint_monitors_error_component import (
            ApiV1WorkspacesUpdateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_gitlab_project_id_error_component import (
            ApiV1WorkspacesUpdateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_gitlab_project_url_error_component import (
            ApiV1WorkspacesUpdateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_update_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesUpdateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_update_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesUpdateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_update_kind_error_component import ApiV1WorkspacesUpdateKindErrorComponent
        from ..models.api_v1_workspaces_update_labels_error_component import ApiV1WorkspacesUpdateLabelsErrorComponent
        from ..models.api_v1_workspaces_update_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_name_error_component import ApiV1WorkspacesUpdateNameErrorComponent
        from ..models.api_v1_workspaces_update_non_field_errors_error_component import (
            ApiV1WorkspacesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_notifications_enabled_error_component import (
            ApiV1WorkspacesUpdateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_on_premise_error_component import (
            ApiV1WorkspacesUpdateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_update_organization_id_error_component import (
            ApiV1WorkspacesUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_owner_id_error_component import (
            ApiV1WorkspacesUpdateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_platform_service_error_component import (
            ApiV1WorkspacesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_update_pop_id_error_component import ApiV1WorkspacesUpdatePopIdErrorComponent
        from ..models.api_v1_workspaces_update_provider_error_component import (
            ApiV1WorkspacesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_update_provider_id_error_component import (
            ApiV1WorkspacesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_provider_reference_error_component import (
            ApiV1WorkspacesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_update_purpose_error_component import ApiV1WorkspacesUpdatePurposeErrorComponent
        from ..models.api_v1_workspaces_update_readme_md_error_component import (
            ApiV1WorkspacesUpdateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_reconciliation_enabled_error_component import (
            ApiV1WorkspacesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_scope_error_component import ApiV1WorkspacesUpdateScopeErrorComponent
        from ..models.api_v1_workspaces_update_secrets_poly_raw_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_update_sla_availability_error_component import (
            ApiV1WorkspacesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_sla_target_error_component import (
            ApiV1WorkspacesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_update_slo_availability_error_component import (
            ApiV1WorkspacesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_slo_target_error_component import (
            ApiV1WorkspacesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_update_target_availability_error_component import (
            ApiV1WorkspacesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_template_error_component import (
            ApiV1WorkspacesUpdateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_update_urls_error_component import ApiV1WorkspacesUpdateUrlsErrorComponent
        from ..models.api_v1_workspaces_update_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesUpdateWorkspaceInventoryRawErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesUpdateActualAvailabilityErrorComponent
                | ApiV1WorkspacesUpdateAlternativeNameErrorComponent
                | ApiV1WorkspacesUpdateAnnotationsErrorComponent
                | ApiV1WorkspacesUpdateArchivedAtErrorComponent
                | ApiV1WorkspacesUpdateArchivedErrorComponent
                | ApiV1WorkspacesUpdateArchivedReasonErrorComponent
                | ApiV1WorkspacesUpdateBackupEnabledErrorComponent
                | ApiV1WorkspacesUpdateCriticalityErrorComponent
                | ApiV1WorkspacesUpdateDebugModeErrorComponent
                | ApiV1WorkspacesUpdateDescriptionErrorComponent
                | ApiV1WorkspacesUpdateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesUpdateDisplayNameErrorComponent
                | ApiV1WorkspacesUpdateEncryptedErrorComponent
                | ApiV1WorkspacesUpdateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesUpdateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesUpdateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesUpdateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesUpdateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesUpdateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesUpdateKindErrorComponent
                | ApiV1WorkspacesUpdateLabelsErrorComponent
                | ApiV1WorkspacesUpdateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesUpdateNameErrorComponent
                | ApiV1WorkspacesUpdateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesUpdateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesUpdateOnPremiseErrorComponent
                | ApiV1WorkspacesUpdateOrganizationIdErrorComponent
                | ApiV1WorkspacesUpdateOwnerIdErrorComponent
                | ApiV1WorkspacesUpdatePlatformServiceErrorComponent
                | ApiV1WorkspacesUpdatePopIdErrorComponent
                | ApiV1WorkspacesUpdateProviderErrorComponent
                | ApiV1WorkspacesUpdateProviderIdErrorComponent
                | ApiV1WorkspacesUpdateProviderReferenceErrorComponent
                | ApiV1WorkspacesUpdatePurposeErrorComponent
                | ApiV1WorkspacesUpdateReadmeMdErrorComponent
                | ApiV1WorkspacesUpdateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesUpdateScopeErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesUpdateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesUpdateSlaTargetErrorComponent
                | ApiV1WorkspacesUpdateSloAvailabilityErrorComponent
                | ApiV1WorkspacesUpdateSloTargetErrorComponent
                | ApiV1WorkspacesUpdateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesUpdateTemplateErrorComponent
                | ApiV1WorkspacesUpdateUrlsErrorComponent
                | ApiV1WorkspacesUpdateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_0 = (
                        ApiV1WorkspacesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_1 = (
                        ApiV1WorkspacesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_2 = (
                        ApiV1WorkspacesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_3 = (
                        ApiV1WorkspacesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_4 = (
                        ApiV1WorkspacesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_5 = (
                        ApiV1WorkspacesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_6 = (
                        ApiV1WorkspacesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_7 = (
                        ApiV1WorkspacesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_8 = (
                        ApiV1WorkspacesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_9 = (
                        ApiV1WorkspacesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_10 = (
                        ApiV1WorkspacesUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_11 = (
                        ApiV1WorkspacesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_12 = (
                        ApiV1WorkspacesUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_13 = (
                        ApiV1WorkspacesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_14 = (
                        ApiV1WorkspacesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_15 = (
                        ApiV1WorkspacesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_16 = (
                        ApiV1WorkspacesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_17 = (
                        ApiV1WorkspacesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_18 = (
                        ApiV1WorkspacesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_19 = (
                        ApiV1WorkspacesUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_20 = (
                        ApiV1WorkspacesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_21 = (
                        ApiV1WorkspacesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_22 = (
                        ApiV1WorkspacesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_23 = (
                        ApiV1WorkspacesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_24 = (
                        ApiV1WorkspacesUpdateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_25 = (
                        ApiV1WorkspacesUpdateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_26 = (
                        ApiV1WorkspacesUpdateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_27 = (
                        ApiV1WorkspacesUpdateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_28 = (
                        ApiV1WorkspacesUpdateGlobalEndpointMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_29 = (
                        ApiV1WorkspacesUpdateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_30 = (
                        ApiV1WorkspacesUpdateNotificationsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_31 = (
                        ApiV1WorkspacesUpdateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_32 = (
                        ApiV1WorkspacesUpdateHasIncompatibleKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_33 = (
                        ApiV1WorkspacesUpdateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_34 = (
                        ApiV1WorkspacesUpdateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_35 = (
                        ApiV1WorkspacesUpdateWorkspaceInventoryRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_36 = (
                        ApiV1WorkspacesUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_37 = (
                        ApiV1WorkspacesUpdateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_38 = (
                        ApiV1WorkspacesUpdatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_39 = (
                        ApiV1WorkspacesUpdateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_40 = (
                        ApiV1WorkspacesUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_41 = (
                        ApiV1WorkspacesUpdatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_42 = (
                        ApiV1WorkspacesUpdateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_43 = (
                        ApiV1WorkspacesUpdateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_error_type_44 = (
                        ApiV1WorkspacesUpdateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_update_error_type_45 = (
                    ApiV1WorkspacesUpdateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_update_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_update_validation_error.additional_properties = d
        return api_v1_workspaces_update_validation_error

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
