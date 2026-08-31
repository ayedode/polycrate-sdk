from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_addon_config_revisions_update_actual_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_addon_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateAddonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_annotations_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_archived_at_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_archived_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_archived_reason_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_block_config_template_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_criticality_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_debug_mode_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_discovery_enabled_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_display_name_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_kind_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_labels_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_name_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_non_field_errors_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_platform_service_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_provider_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_provider_id_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_provider_reference_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_scope_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_sla_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_sla_target_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_slo_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_slo_target_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_target_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_update_version_error_component import (
        ApiV1KubernetesAddonConfigRevisionsUpdateVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAddonConfigRevisionsUpdateValidationError")


@_attrs_define
class ApiV1KubernetesAddonConfigRevisionsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAddonConfigRevisionsUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateAddonErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateArchivedAtErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateArchivedErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateBlockConfigTemplateErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateCriticalityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateDebugModeErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateDisplayNameErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateKindErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateLabelsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateNameErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateProviderErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateProviderIdErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateScopeErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateSlaTargetErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateSloTargetErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsUpdateVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAddonConfigRevisionsUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateAddonErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateArchivedAtErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateArchivedErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateBlockConfigTemplateErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateCriticalityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateDebugModeErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateDisplayNameErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateKindErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateLabelsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateNameErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateProviderErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateProviderIdErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateScopeErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateSlaTargetErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateSloTargetErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsUpdateVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_addon_config_revisions_update_actual_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_addon_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_annotations_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_archived_at_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_archived_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_archived_reason_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_criticality_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_debug_mode_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_discovery_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_display_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_kind_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_labels_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_non_field_errors_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_platform_service_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_provider_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_provider_id_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_provider_reference_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_scope_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_sla_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_sla_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_slo_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_slo_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_target_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_version_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateAddonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsUpdateVersionErrorComponent):
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
        from ..models.api_v1_kubernetes_addon_config_revisions_update_actual_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_addon_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_annotations_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_archived_at_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_archived_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_archived_reason_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_block_config_template_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_criticality_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_debug_mode_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_discovery_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_display_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_kind_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_labels_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_non_field_errors_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_platform_service_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_provider_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_provider_id_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_provider_reference_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_scope_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_sla_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_sla_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_slo_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_slo_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_target_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_update_version_error_component import (
            ApiV1KubernetesAddonConfigRevisionsUpdateVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAddonConfigRevisionsUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateAddonErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateArchivedAtErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateArchivedErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateBlockConfigTemplateErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateCriticalityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateDebugModeErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateDisplayNameErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateKindErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateLabelsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateNameErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateProviderErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateProviderIdErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateScopeErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateSlaTargetErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateSloTargetErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsUpdateVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_0 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_1 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_2 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_3 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_4 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_5 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_6 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_7 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_8 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_9 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_10 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_11 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_12 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_13 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_14 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_15 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_16 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_17 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_18 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_19 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_20 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_21 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_22 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_23 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_24 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateAddonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_25 = (
                        ApiV1KubernetesAddonConfigRevisionsUpdateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_26 = (
                    ApiV1KubernetesAddonConfigRevisionsUpdateBlockConfigTemplateErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_addon_config_revisions_update_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_addon_config_revisions_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_addon_config_revisions_update_validation_error.additional_properties = d
        return api_v1_kubernetes_addon_config_revisions_update_validation_error

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
