from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_actual_availability_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_alternative_name_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_annotations_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_archived_at_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_archived_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_archived_reason_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_backup_enabled_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_criticality_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_debug_mode_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_description_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_discovery_enabled_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_display_name_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_encrypted_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_endpoint_monitors_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_gitlab_project_id_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_gitlab_project_url_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_kind_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_labels_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_name_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_non_field_errors_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_notifications_enabled_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_on_premise_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_organization_id_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_owner_id_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOwnerIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_platform_service_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_pop_id_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePopIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_provider_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_provider_id_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_provider_reference_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_purpose_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePurposeErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_readme_md_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReadmeMdErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_reconciliation_enabled_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_scope_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_secrets_poly_raw_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_sla_availability_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_sla_target_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_slo_availability_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_slo_target_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_target_availability_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_template_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTemplateErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_urls_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateUrlsErrorComponent,
    )
    from ..models.api_v1_workspaces_update_secrets_poly_partial_update_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesUpdateSecretsPolyPartialUpdateValidationError")


@_attrs_define
class ApiV1WorkspacesUpdateSecretsPolyPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesUpdateSecretsPolyPartialUpdateActualAvailabilityErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAlternativeNameErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAnnotationsErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedAtErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedReasonErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateBackupEnabledErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateCriticalityErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDebugModeErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDescriptionErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDisplayNameErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitoringModeErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitorsErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectIdErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateHasIncompatibleKubeconfigErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateKindErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateLabelsErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNameErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNotificationsEnabledErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOnPremiseErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOrganizationIdErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOwnerIdErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePlatformServiceErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePopIdErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderIdErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderReferenceErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePurposeErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReadmeMdErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateScopeErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSecretsPolyRawErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaTargetErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloAvailabilityErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloTargetErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTemplateErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateUrlsErrorComponent |
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateActualAvailabilityErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAlternativeNameErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAnnotationsErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedAtErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedReasonErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateBackupEnabledErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateCriticalityErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDebugModeErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDescriptionErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDisplayNameErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateKindErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateLabelsErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNameErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOnPremiseErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOrganizationIdErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOwnerIdErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePlatformServiceErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePopIdErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderIdErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderReferenceErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePurposeErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReadmeMdErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateScopeErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaTargetErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloAvailabilityErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloTargetErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTemplateErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateUrlsErrorComponent
        | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_actual_availability_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_annotations_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_archived_at_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_archived_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_archived_reason_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_backup_enabled_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_criticality_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_debug_mode_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_description_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_discovery_enabled_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_display_name_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_encrypted_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_endpoint_monitors_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_gitlab_project_id_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_gitlab_project_url_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_kind_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_labels_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_name_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_non_field_errors_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_notifications_enabled_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_on_premise_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_organization_id_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_owner_id_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_platform_service_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_pop_id_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_provider_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_provider_id_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_provider_reference_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_purpose_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_readme_md_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_reconciliation_enabled_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_scope_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_secrets_poly_raw_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_sla_availability_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_sla_target_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_slo_availability_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_slo_target_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_target_availability_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_template_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_urls_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateWorkspaceInventoryRawErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderReferenceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDiscoveryEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePlatformServiceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedReasonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectIdErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectUrlErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitoringModeErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data,
                ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNotificationsEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateBackupEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateHasIncompatibleKubeconfigErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitorsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSecretsPolyRawErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateWorkspaceInventoryRawErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOrganizationIdErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReadmeMdErrorComponent):
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
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_actual_availability_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_alternative_name_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAlternativeNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_annotations_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_archived_at_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_archived_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_archived_reason_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_backup_enabled_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_criticality_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_debug_mode_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_description_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_discovery_enabled_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_display_name_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_encrypted_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_endpoint_monitors_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_gitlab_project_id_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_gitlab_project_url_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_kind_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_labels_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_name_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_non_field_errors_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_notifications_enabled_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_on_premise_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_organization_id_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_owner_id_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_platform_service_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_pop_id_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_provider_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_provider_id_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_provider_reference_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_purpose_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_readme_md_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_reconciliation_enabled_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_scope_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_secrets_poly_raw_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_sla_availability_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_sla_target_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_slo_availability_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_slo_target_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_target_availability_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_template_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_urls_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_update_secrets_poly_partial_update_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesUpdateSecretsPolyPartialUpdateWorkspaceInventoryRawErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesUpdateSecretsPolyPartialUpdateActualAvailabilityErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAlternativeNameErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAnnotationsErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedAtErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedReasonErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateBackupEnabledErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateCriticalityErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDebugModeErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDescriptionErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDisplayNameErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateKindErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateLabelsErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNameErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOnPremiseErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOrganizationIdErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOwnerIdErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePlatformServiceErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePopIdErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderIdErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderReferenceErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePurposeErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReadmeMdErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateScopeErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaTargetErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloAvailabilityErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloTargetErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTemplateErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateUrlsErrorComponent
                | ApiV1WorkspacesUpdateSecretsPolyPartialUpdateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_0 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_1 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_2 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_3 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_4 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_5 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_6 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_7 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_8 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_9 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_10 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_11 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_12 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_13 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_14 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_15 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_16 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_17 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_18 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_19 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_20 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_21 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_22 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_23 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_24 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_25 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_26 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_27 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitoringModeErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_28 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_29 = ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_30 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateNotificationsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_31 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_32 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateHasIncompatibleKubeconfigErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_33 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_34 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_35 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateWorkspaceInventoryRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_36 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_37 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_38 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_39 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_40 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_41 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_42 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_43 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_44 = (
                        ApiV1WorkspacesUpdateSecretsPolyPartialUpdateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_45 = (
                    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_update_secrets_poly_partial_update_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_update_secrets_poly_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_update_secrets_poly_partial_update_validation_error.additional_properties = d
        return api_v1_workspaces_update_secrets_poly_partial_update_validation_error

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
