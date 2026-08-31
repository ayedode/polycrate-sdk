from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_actual_availability_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_alternative_name_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_annotations_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_archived_at_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_archived_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_archived_reason_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_backup_enabled_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_criticality_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_debug_mode_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_description_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_discovery_enabled_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_display_name_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_encrypted_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEncryptedErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_endpoint_monitors_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_gitlab_project_id_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_gitlab_project_url_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_kind_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_labels_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_name_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_non_field_errors_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_notifications_enabled_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_on_premise_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_organization_id_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_owner_id_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOwnerIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_platform_service_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_pop_id_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePopIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_provider_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_provider_id_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_provider_reference_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_purpose_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_readme_md_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReadmeMdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_reconciliation_enabled_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_scope_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_secrets_poly_raw_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_sla_availability_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_sla_target_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_slo_availability_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_slo_target_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_target_availability_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_template_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTemplateErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_urls_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateUrlsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_workspace_poly_partial_update_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateValidationError")


@_attrs_define
class ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateActualAvailabilityErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAlternativeNameErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAnnotationsErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedAtErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedReasonErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateBackupEnabledErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateCriticalityErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDebugModeErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDescriptionErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDisplayNameErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEncryptedErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitoringModeErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitorsErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectIdErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateHasIncompatibleKubeconfigErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateKindErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateLabelsErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNameErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNotificationsEnabledErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOnPremiseErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOrganizationIdErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOwnerIdErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePlatformServiceErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePopIdErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderIdErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderReferenceErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReadmeMdErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateScopeErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSecretsPolyRawErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaTargetErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloAvailabilityErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloTargetErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTemplateErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateUrlsErrorComponent |
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateActualAvailabilityErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAlternativeNameErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAnnotationsErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedAtErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedReasonErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateBackupEnabledErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateCriticalityErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDebugModeErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDescriptionErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDisplayNameErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEncryptedErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateKindErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateLabelsErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNameErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOnPremiseErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOrganizationIdErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOwnerIdErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePlatformServiceErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePopIdErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderIdErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderReferenceErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReadmeMdErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateScopeErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaTargetErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloAvailabilityErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloTargetErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTemplateErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateUrlsErrorComponent
        | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_actual_availability_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_annotations_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_archived_at_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_archived_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_archived_reason_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_backup_enabled_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_criticality_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_debug_mode_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_description_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_discovery_enabled_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_display_name_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_encrypted_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_endpoint_monitors_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_gitlab_project_id_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_gitlab_project_url_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_kind_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_labels_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_name_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_non_field_errors_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_notifications_enabled_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_on_premise_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_organization_id_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_owner_id_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_platform_service_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_pop_id_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_provider_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_provider_id_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_provider_reference_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_purpose_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_readme_md_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_reconciliation_enabled_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_scope_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_secrets_poly_raw_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_sla_availability_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_sla_target_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_slo_availability_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_slo_target_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_target_availability_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_template_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_urls_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateWorkspaceInventoryRawErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNonFieldErrorsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderReferenceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDiscoveryEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePlatformServiceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedReasonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectIdErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectUrlErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitoringModeErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGlobalEndpointMonitorErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data,
                ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNotificationsEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateBackupEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateHasIncompatibleKubeconfigErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitorsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSecretsPolyRawErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateWorkspaceInventoryRawErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOrganizationIdErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReadmeMdErrorComponent):
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
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_actual_availability_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_alternative_name_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAlternativeNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_annotations_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_archived_at_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_archived_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_archived_reason_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_backup_enabled_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_criticality_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_debug_mode_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_description_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_discovery_enabled_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_display_name_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_encrypted_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_endpoint_monitors_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_gitlab_project_id_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_gitlab_project_url_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_kind_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_labels_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_name_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_non_field_errors_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_notifications_enabled_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_on_premise_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_organization_id_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_owner_id_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_platform_service_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_pop_id_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_provider_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_provider_id_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_provider_reference_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_purpose_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_readme_md_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_reconciliation_enabled_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_scope_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_secrets_poly_raw_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_sla_availability_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_sla_target_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_slo_availability_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_slo_target_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_target_availability_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_template_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_urls_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_workspace_poly_partial_update_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateWorkspaceInventoryRawErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateActualAvailabilityErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAlternativeNameErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAnnotationsErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedAtErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedReasonErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateBackupEnabledErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateCriticalityErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDebugModeErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDescriptionErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDisplayNameErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEncryptedErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateKindErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateLabelsErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNameErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOnPremiseErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOrganizationIdErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOwnerIdErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePlatformServiceErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePopIdErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderIdErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderReferenceErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReadmeMdErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateScopeErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaTargetErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloAvailabilityErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloTargetErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTemplateErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateUrlsErrorComponent
                | ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_0 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_1 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_2 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_3 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_4 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_5 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_6 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_7 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_8 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_9 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReconciliationEnabledErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_10 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_11 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_12 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_13 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_14 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_15 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_16 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_17 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_18 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_19 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_20 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_21 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_22 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_23 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_24 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_25 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_26 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_27 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitoringModeErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_28 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGlobalEndpointMonitorErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_29 = ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_30 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateNotificationsEnabledErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_31 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_32 = ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateHasIncompatibleKubeconfigErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_33 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_34 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_35 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateWorkspaceInventoryRawErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_36 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_37 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_38 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_39 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_40 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_41 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_42 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_43 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_44 = (
                        ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_45 = (
                    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_update_workspace_poly_partial_update_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_update_workspace_poly_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_update_workspace_poly_partial_update_validation_error.additional_properties = d
        return api_v1_workspaces_update_workspace_poly_partial_update_validation_error

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
