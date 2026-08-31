from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_partial_update_actual_availability_error_component import (
        ApiV1WorkspacesPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_alternative_name_error_component import (
        ApiV1WorkspacesPartialUpdateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_annotations_error_component import (
        ApiV1WorkspacesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_archived_at_error_component import (
        ApiV1WorkspacesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_archived_error_component import (
        ApiV1WorkspacesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_archived_reason_error_component import (
        ApiV1WorkspacesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_backup_enabled_error_component import (
        ApiV1WorkspacesPartialUpdateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_criticality_error_component import (
        ApiV1WorkspacesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_debug_mode_error_component import (
        ApiV1WorkspacesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_description_error_component import (
        ApiV1WorkspacesPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_discovery_enabled_error_component import (
        ApiV1WorkspacesPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_display_name_error_component import (
        ApiV1WorkspacesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_encrypted_error_component import (
        ApiV1WorkspacesPartialUpdateEncryptedErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesPartialUpdateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_endpoint_monitors_error_component import (
        ApiV1WorkspacesPartialUpdateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_gitlab_project_id_error_component import (
        ApiV1WorkspacesPartialUpdateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_gitlab_project_url_error_component import (
        ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesPartialUpdateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesPartialUpdateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_kind_error_component import (
        ApiV1WorkspacesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_labels_error_component import (
        ApiV1WorkspacesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_name_error_component import (
        ApiV1WorkspacesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_non_field_errors_error_component import (
        ApiV1WorkspacesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_notifications_enabled_error_component import (
        ApiV1WorkspacesPartialUpdateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_on_premise_error_component import (
        ApiV1WorkspacesPartialUpdateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_organization_id_error_component import (
        ApiV1WorkspacesPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_owner_id_error_component import (
        ApiV1WorkspacesPartialUpdateOwnerIdErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_platform_service_error_component import (
        ApiV1WorkspacesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_pop_id_error_component import (
        ApiV1WorkspacesPartialUpdatePopIdErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_provider_error_component import (
        ApiV1WorkspacesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_provider_id_error_component import (
        ApiV1WorkspacesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_provider_reference_error_component import (
        ApiV1WorkspacesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_purpose_error_component import (
        ApiV1WorkspacesPartialUpdatePurposeErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_readme_md_error_component import (
        ApiV1WorkspacesPartialUpdateReadmeMdErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_reconciliation_enabled_error_component import (
        ApiV1WorkspacesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_scope_error_component import (
        ApiV1WorkspacesPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_secrets_poly_raw_error_component import (
        ApiV1WorkspacesPartialUpdateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_sla_availability_error_component import (
        ApiV1WorkspacesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_sla_target_error_component import (
        ApiV1WorkspacesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_slo_availability_error_component import (
        ApiV1WorkspacesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_slo_target_error_component import (
        ApiV1WorkspacesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_target_availability_error_component import (
        ApiV1WorkspacesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_template_error_component import (
        ApiV1WorkspacesPartialUpdateTemplateErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_urls_error_component import (
        ApiV1WorkspacesPartialUpdateUrlsErrorComponent,
    )
    from ..models.api_v1_workspaces_partial_update_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesPartialUpdateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesPartialUpdateValidationError")


@_attrs_define
class ApiV1WorkspacesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesPartialUpdateActualAvailabilityErrorComponent |
            ApiV1WorkspacesPartialUpdateAlternativeNameErrorComponent |
            ApiV1WorkspacesPartialUpdateAnnotationsErrorComponent | ApiV1WorkspacesPartialUpdateArchivedAtErrorComponent |
            ApiV1WorkspacesPartialUpdateArchivedErrorComponent | ApiV1WorkspacesPartialUpdateArchivedReasonErrorComponent |
            ApiV1WorkspacesPartialUpdateBackupEnabledErrorComponent | ApiV1WorkspacesPartialUpdateCriticalityErrorComponent
            | ApiV1WorkspacesPartialUpdateDebugModeErrorComponent | ApiV1WorkspacesPartialUpdateDescriptionErrorComponent |
            ApiV1WorkspacesPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1WorkspacesPartialUpdateDisplayNameErrorComponent | ApiV1WorkspacesPartialUpdateEncryptedErrorComponent |
            ApiV1WorkspacesPartialUpdateEndpointMonitoringModeErrorComponent |
            ApiV1WorkspacesPartialUpdateEndpointMonitorsErrorComponent |
            ApiV1WorkspacesPartialUpdateGitlabProjectIdErrorComponent |
            ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesPartialUpdateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesPartialUpdateHasIncompatibleKubeconfigErrorComponent |
            ApiV1WorkspacesPartialUpdateKindErrorComponent | ApiV1WorkspacesPartialUpdateLabelsErrorComponent |
            ApiV1WorkspacesPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesPartialUpdateNameErrorComponent | ApiV1WorkspacesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1WorkspacesPartialUpdateNotificationsEnabledErrorComponent |
            ApiV1WorkspacesPartialUpdateOnPremiseErrorComponent | ApiV1WorkspacesPartialUpdateOrganizationIdErrorComponent |
            ApiV1WorkspacesPartialUpdateOwnerIdErrorComponent | ApiV1WorkspacesPartialUpdatePlatformServiceErrorComponent |
            ApiV1WorkspacesPartialUpdatePopIdErrorComponent | ApiV1WorkspacesPartialUpdateProviderErrorComponent |
            ApiV1WorkspacesPartialUpdateProviderIdErrorComponent |
            ApiV1WorkspacesPartialUpdateProviderReferenceErrorComponent | ApiV1WorkspacesPartialUpdatePurposeErrorComponent
            | ApiV1WorkspacesPartialUpdateReadmeMdErrorComponent |
            ApiV1WorkspacesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1WorkspacesPartialUpdateScopeErrorComponent | ApiV1WorkspacesPartialUpdateSecretsPolyRawErrorComponent |
            ApiV1WorkspacesPartialUpdateSlaAvailabilityErrorComponent | ApiV1WorkspacesPartialUpdateSlaTargetErrorComponent
            | ApiV1WorkspacesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1WorkspacesPartialUpdateSloTargetErrorComponent |
            ApiV1WorkspacesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1WorkspacesPartialUpdateTemplateErrorComponent | ApiV1WorkspacesPartialUpdateUrlsErrorComponent |
            ApiV1WorkspacesPartialUpdateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesPartialUpdateActualAvailabilityErrorComponent
        | ApiV1WorkspacesPartialUpdateAlternativeNameErrorComponent
        | ApiV1WorkspacesPartialUpdateAnnotationsErrorComponent
        | ApiV1WorkspacesPartialUpdateArchivedAtErrorComponent
        | ApiV1WorkspacesPartialUpdateArchivedErrorComponent
        | ApiV1WorkspacesPartialUpdateArchivedReasonErrorComponent
        | ApiV1WorkspacesPartialUpdateBackupEnabledErrorComponent
        | ApiV1WorkspacesPartialUpdateCriticalityErrorComponent
        | ApiV1WorkspacesPartialUpdateDebugModeErrorComponent
        | ApiV1WorkspacesPartialUpdateDescriptionErrorComponent
        | ApiV1WorkspacesPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesPartialUpdateDisplayNameErrorComponent
        | ApiV1WorkspacesPartialUpdateEncryptedErrorComponent
        | ApiV1WorkspacesPartialUpdateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesPartialUpdateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesPartialUpdateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesPartialUpdateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesPartialUpdateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesPartialUpdateKindErrorComponent
        | ApiV1WorkspacesPartialUpdateLabelsErrorComponent
        | ApiV1WorkspacesPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesPartialUpdateNameErrorComponent
        | ApiV1WorkspacesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesPartialUpdateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesPartialUpdateOnPremiseErrorComponent
        | ApiV1WorkspacesPartialUpdateOrganizationIdErrorComponent
        | ApiV1WorkspacesPartialUpdateOwnerIdErrorComponent
        | ApiV1WorkspacesPartialUpdatePlatformServiceErrorComponent
        | ApiV1WorkspacesPartialUpdatePopIdErrorComponent
        | ApiV1WorkspacesPartialUpdateProviderErrorComponent
        | ApiV1WorkspacesPartialUpdateProviderIdErrorComponent
        | ApiV1WorkspacesPartialUpdateProviderReferenceErrorComponent
        | ApiV1WorkspacesPartialUpdatePurposeErrorComponent
        | ApiV1WorkspacesPartialUpdateReadmeMdErrorComponent
        | ApiV1WorkspacesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesPartialUpdateScopeErrorComponent
        | ApiV1WorkspacesPartialUpdateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesPartialUpdateSlaTargetErrorComponent
        | ApiV1WorkspacesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1WorkspacesPartialUpdateSloTargetErrorComponent
        | ApiV1WorkspacesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesPartialUpdateTemplateErrorComponent
        | ApiV1WorkspacesPartialUpdateUrlsErrorComponent
        | ApiV1WorkspacesPartialUpdateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_partial_update_actual_availability_error_component import (
            ApiV1WorkspacesPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_annotations_error_component import (
            ApiV1WorkspacesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_archived_at_error_component import (
            ApiV1WorkspacesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_archived_error_component import (
            ApiV1WorkspacesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_archived_reason_error_component import (
            ApiV1WorkspacesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_backup_enabled_error_component import (
            ApiV1WorkspacesPartialUpdateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_criticality_error_component import (
            ApiV1WorkspacesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_debug_mode_error_component import (
            ApiV1WorkspacesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_description_error_component import (
            ApiV1WorkspacesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_discovery_enabled_error_component import (
            ApiV1WorkspacesPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_display_name_error_component import (
            ApiV1WorkspacesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_encrypted_error_component import (
            ApiV1WorkspacesPartialUpdateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesPartialUpdateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_endpoint_monitors_error_component import (
            ApiV1WorkspacesPartialUpdateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_gitlab_project_id_error_component import (
            ApiV1WorkspacesPartialUpdateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_gitlab_project_url_error_component import (
            ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesPartialUpdateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesPartialUpdateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_kind_error_component import (
            ApiV1WorkspacesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_labels_error_component import (
            ApiV1WorkspacesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_name_error_component import (
            ApiV1WorkspacesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_non_field_errors_error_component import (
            ApiV1WorkspacesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_notifications_enabled_error_component import (
            ApiV1WorkspacesPartialUpdateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_on_premise_error_component import (
            ApiV1WorkspacesPartialUpdateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_organization_id_error_component import (
            ApiV1WorkspacesPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_owner_id_error_component import (
            ApiV1WorkspacesPartialUpdateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_platform_service_error_component import (
            ApiV1WorkspacesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_pop_id_error_component import (
            ApiV1WorkspacesPartialUpdatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_provider_error_component import (
            ApiV1WorkspacesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_provider_id_error_component import (
            ApiV1WorkspacesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_provider_reference_error_component import (
            ApiV1WorkspacesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_purpose_error_component import (
            ApiV1WorkspacesPartialUpdatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_readme_md_error_component import (
            ApiV1WorkspacesPartialUpdateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_reconciliation_enabled_error_component import (
            ApiV1WorkspacesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_scope_error_component import (
            ApiV1WorkspacesPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_secrets_poly_raw_error_component import (
            ApiV1WorkspacesPartialUpdateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_sla_availability_error_component import (
            ApiV1WorkspacesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_sla_target_error_component import (
            ApiV1WorkspacesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_slo_availability_error_component import (
            ApiV1WorkspacesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_slo_target_error_component import (
            ApiV1WorkspacesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_target_availability_error_component import (
            ApiV1WorkspacesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_template_error_component import (
            ApiV1WorkspacesPartialUpdateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_urls_error_component import (
            ApiV1WorkspacesPartialUpdateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesPartialUpdateWorkspaceInventoryRawErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateGlobalEndpointMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateNotificationsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateBackupEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateHasIncompatibleKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateEndpointMonitorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateSecretsPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateWorkspaceInventoryRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesPartialUpdateReadmeMdErrorComponent):
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
        from ..models.api_v1_workspaces_partial_update_actual_availability_error_component import (
            ApiV1WorkspacesPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_alternative_name_error_component import (
            ApiV1WorkspacesPartialUpdateAlternativeNameErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_annotations_error_component import (
            ApiV1WorkspacesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_archived_at_error_component import (
            ApiV1WorkspacesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_archived_error_component import (
            ApiV1WorkspacesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_archived_reason_error_component import (
            ApiV1WorkspacesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_backup_enabled_error_component import (
            ApiV1WorkspacesPartialUpdateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_criticality_error_component import (
            ApiV1WorkspacesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_debug_mode_error_component import (
            ApiV1WorkspacesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_description_error_component import (
            ApiV1WorkspacesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_discovery_enabled_error_component import (
            ApiV1WorkspacesPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_display_name_error_component import (
            ApiV1WorkspacesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_encrypted_error_component import (
            ApiV1WorkspacesPartialUpdateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesPartialUpdateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_endpoint_monitors_error_component import (
            ApiV1WorkspacesPartialUpdateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_gitlab_project_id_error_component import (
            ApiV1WorkspacesPartialUpdateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_gitlab_project_url_error_component import (
            ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesPartialUpdateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesPartialUpdateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_kind_error_component import (
            ApiV1WorkspacesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_labels_error_component import (
            ApiV1WorkspacesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_name_error_component import (
            ApiV1WorkspacesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_non_field_errors_error_component import (
            ApiV1WorkspacesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_notifications_enabled_error_component import (
            ApiV1WorkspacesPartialUpdateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_on_premise_error_component import (
            ApiV1WorkspacesPartialUpdateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_organization_id_error_component import (
            ApiV1WorkspacesPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_owner_id_error_component import (
            ApiV1WorkspacesPartialUpdateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_platform_service_error_component import (
            ApiV1WorkspacesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_pop_id_error_component import (
            ApiV1WorkspacesPartialUpdatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_provider_error_component import (
            ApiV1WorkspacesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_provider_id_error_component import (
            ApiV1WorkspacesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_provider_reference_error_component import (
            ApiV1WorkspacesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_purpose_error_component import (
            ApiV1WorkspacesPartialUpdatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_readme_md_error_component import (
            ApiV1WorkspacesPartialUpdateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_reconciliation_enabled_error_component import (
            ApiV1WorkspacesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_scope_error_component import (
            ApiV1WorkspacesPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_secrets_poly_raw_error_component import (
            ApiV1WorkspacesPartialUpdateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_sla_availability_error_component import (
            ApiV1WorkspacesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_sla_target_error_component import (
            ApiV1WorkspacesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_slo_availability_error_component import (
            ApiV1WorkspacesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_slo_target_error_component import (
            ApiV1WorkspacesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_target_availability_error_component import (
            ApiV1WorkspacesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_template_error_component import (
            ApiV1WorkspacesPartialUpdateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_urls_error_component import (
            ApiV1WorkspacesPartialUpdateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_partial_update_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesPartialUpdateWorkspaceInventoryRawErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesPartialUpdateActualAvailabilityErrorComponent
                | ApiV1WorkspacesPartialUpdateAlternativeNameErrorComponent
                | ApiV1WorkspacesPartialUpdateAnnotationsErrorComponent
                | ApiV1WorkspacesPartialUpdateArchivedAtErrorComponent
                | ApiV1WorkspacesPartialUpdateArchivedErrorComponent
                | ApiV1WorkspacesPartialUpdateArchivedReasonErrorComponent
                | ApiV1WorkspacesPartialUpdateBackupEnabledErrorComponent
                | ApiV1WorkspacesPartialUpdateCriticalityErrorComponent
                | ApiV1WorkspacesPartialUpdateDebugModeErrorComponent
                | ApiV1WorkspacesPartialUpdateDescriptionErrorComponent
                | ApiV1WorkspacesPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesPartialUpdateDisplayNameErrorComponent
                | ApiV1WorkspacesPartialUpdateEncryptedErrorComponent
                | ApiV1WorkspacesPartialUpdateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesPartialUpdateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesPartialUpdateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesPartialUpdateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesPartialUpdateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesPartialUpdateKindErrorComponent
                | ApiV1WorkspacesPartialUpdateLabelsErrorComponent
                | ApiV1WorkspacesPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesPartialUpdateNameErrorComponent
                | ApiV1WorkspacesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesPartialUpdateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesPartialUpdateOnPremiseErrorComponent
                | ApiV1WorkspacesPartialUpdateOrganizationIdErrorComponent
                | ApiV1WorkspacesPartialUpdateOwnerIdErrorComponent
                | ApiV1WorkspacesPartialUpdatePlatformServiceErrorComponent
                | ApiV1WorkspacesPartialUpdatePopIdErrorComponent
                | ApiV1WorkspacesPartialUpdateProviderErrorComponent
                | ApiV1WorkspacesPartialUpdateProviderIdErrorComponent
                | ApiV1WorkspacesPartialUpdateProviderReferenceErrorComponent
                | ApiV1WorkspacesPartialUpdatePurposeErrorComponent
                | ApiV1WorkspacesPartialUpdateReadmeMdErrorComponent
                | ApiV1WorkspacesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesPartialUpdateScopeErrorComponent
                | ApiV1WorkspacesPartialUpdateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesPartialUpdateSlaTargetErrorComponent
                | ApiV1WorkspacesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1WorkspacesPartialUpdateSloTargetErrorComponent
                | ApiV1WorkspacesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesPartialUpdateTemplateErrorComponent
                | ApiV1WorkspacesPartialUpdateUrlsErrorComponent
                | ApiV1WorkspacesPartialUpdateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_0 = (
                        ApiV1WorkspacesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_1 = (
                        ApiV1WorkspacesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_2 = (
                        ApiV1WorkspacesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_3 = (
                        ApiV1WorkspacesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_4 = (
                        ApiV1WorkspacesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_5 = (
                        ApiV1WorkspacesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_6 = (
                        ApiV1WorkspacesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_7 = (
                        ApiV1WorkspacesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_8 = (
                        ApiV1WorkspacesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_9 = (
                        ApiV1WorkspacesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_10 = (
                        ApiV1WorkspacesPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_11 = (
                        ApiV1WorkspacesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_12 = (
                        ApiV1WorkspacesPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_13 = (
                        ApiV1WorkspacesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_14 = (
                        ApiV1WorkspacesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_15 = (
                        ApiV1WorkspacesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_16 = (
                        ApiV1WorkspacesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_17 = (
                        ApiV1WorkspacesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_18 = (
                        ApiV1WorkspacesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_19 = (
                        ApiV1WorkspacesPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_20 = (
                        ApiV1WorkspacesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_21 = (
                        ApiV1WorkspacesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_22 = (
                        ApiV1WorkspacesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_23 = (
                        ApiV1WorkspacesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_24 = (
                        ApiV1WorkspacesPartialUpdateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_25 = (
                        ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_26 = (
                        ApiV1WorkspacesPartialUpdateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_27 = (
                        ApiV1WorkspacesPartialUpdateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_28 = (
                        ApiV1WorkspacesPartialUpdateGlobalEndpointMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_29 = (
                        ApiV1WorkspacesPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_30 = (
                        ApiV1WorkspacesPartialUpdateNotificationsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_31 = (
                        ApiV1WorkspacesPartialUpdateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_32 = (
                        ApiV1WorkspacesPartialUpdateHasIncompatibleKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_33 = (
                        ApiV1WorkspacesPartialUpdateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_34 = (
                        ApiV1WorkspacesPartialUpdateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_35 = (
                        ApiV1WorkspacesPartialUpdateWorkspaceInventoryRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_36 = (
                        ApiV1WorkspacesPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_37 = (
                        ApiV1WorkspacesPartialUpdateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_38 = (
                        ApiV1WorkspacesPartialUpdatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_39 = (
                        ApiV1WorkspacesPartialUpdateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_40 = (
                        ApiV1WorkspacesPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_41 = (
                        ApiV1WorkspacesPartialUpdatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_42 = (
                        ApiV1WorkspacesPartialUpdateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_43 = (
                        ApiV1WorkspacesPartialUpdateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_partial_update_error_type_44 = (
                        ApiV1WorkspacesPartialUpdateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_partial_update_error_type_45 = (
                    ApiV1WorkspacesPartialUpdateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_partial_update_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_partial_update_validation_error.additional_properties = d
        return api_v1_workspaces_partial_update_validation_error

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
