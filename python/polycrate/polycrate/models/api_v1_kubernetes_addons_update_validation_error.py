from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_addons_update_actual_availability_error_component import (
        ApiV1KubernetesAddonsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_allow_multiple_error_component import (
        ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_annotations_error_component import (
        ApiV1KubernetesAddonsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_archived_at_error_component import (
        ApiV1KubernetesAddonsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_archived_error_component import (
        ApiV1KubernetesAddonsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_archived_reason_error_component import (
        ApiV1KubernetesAddonsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_block_name_error_component import (
        ApiV1KubernetesAddonsUpdateBlockNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_catalogue_app_error_component import (
        ApiV1KubernetesAddonsUpdateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_criticality_error_component import (
        ApiV1KubernetesAddonsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_debug_mode_error_component import (
        ApiV1KubernetesAddonsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_default_block_config_template_error_component import (
        ApiV1KubernetesAddonsUpdateDefaultBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_default_version_error_component import (
        ApiV1KubernetesAddonsUpdateDefaultVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_discovery_enabled_error_component import (
        ApiV1KubernetesAddonsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_display_name_error_component import (
        ApiV1KubernetesAddonsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_enforcement_error_component import (
        ApiV1KubernetesAddonsUpdateEnforcementErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_is_default_error_component import (
        ApiV1KubernetesAddonsUpdateIsDefaultErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_kind_error_component import (
        ApiV1KubernetesAddonsUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_labels_error_component import (
        ApiV1KubernetesAddonsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_name_error_component import (
        ApiV1KubernetesAddonsUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_non_field_errors_error_component import (
        ApiV1KubernetesAddonsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_order_error_component import (
        ApiV1KubernetesAddonsUpdateOrderErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_platform_service_error_component import (
        ApiV1KubernetesAddonsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_provider_error_component import (
        ApiV1KubernetesAddonsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_provider_id_error_component import (
        ApiV1KubernetesAddonsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_provider_reference_error_component import (
        ApiV1KubernetesAddonsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesAddonsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_scope_error_component import (
        ApiV1KubernetesAddonsUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_scope_expressions_error_component import (
        ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_sla_availability_error_component import (
        ApiV1KubernetesAddonsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_sla_target_error_component import (
        ApiV1KubernetesAddonsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_slo_availability_error_component import (
        ApiV1KubernetesAddonsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_slo_target_error_component import (
        ApiV1KubernetesAddonsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_target_availability_error_component import (
        ApiV1KubernetesAddonsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_update_template_block_error_component import (
        ApiV1KubernetesAddonsUpdateTemplateBlockErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAddonsUpdateValidationError")


@_attrs_define
class ApiV1KubernetesAddonsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAddonsUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponent | ApiV1KubernetesAddonsUpdateAnnotationsErrorComponent |
            ApiV1KubernetesAddonsUpdateArchivedAtErrorComponent | ApiV1KubernetesAddonsUpdateArchivedErrorComponent |
            ApiV1KubernetesAddonsUpdateArchivedReasonErrorComponent | ApiV1KubernetesAddonsUpdateBlockNameErrorComponent |
            ApiV1KubernetesAddonsUpdateCatalogueAppErrorComponent | ApiV1KubernetesAddonsUpdateCriticalityErrorComponent |
            ApiV1KubernetesAddonsUpdateDebugModeErrorComponent |
            ApiV1KubernetesAddonsUpdateDefaultBlockConfigTemplateErrorComponent |
            ApiV1KubernetesAddonsUpdateDefaultVersionErrorComponent |
            ApiV1KubernetesAddonsUpdateDiscoveryEnabledErrorComponent | ApiV1KubernetesAddonsUpdateDisplayNameErrorComponent
            | ApiV1KubernetesAddonsUpdateEnforcementErrorComponent | ApiV1KubernetesAddonsUpdateIsDefaultErrorComponent |
            ApiV1KubernetesAddonsUpdateKindErrorComponent | ApiV1KubernetesAddonsUpdateLabelsErrorComponent |
            ApiV1KubernetesAddonsUpdateNameErrorComponent | ApiV1KubernetesAddonsUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAddonsUpdateOrderErrorComponent | ApiV1KubernetesAddonsUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesAddonsUpdateProviderErrorComponent | ApiV1KubernetesAddonsUpdateProviderIdErrorComponent |
            ApiV1KubernetesAddonsUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesAddonsUpdateReconciliationEnabledErrorComponent | ApiV1KubernetesAddonsUpdateScopeErrorComponent
            | ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponent |
            ApiV1KubernetesAddonsUpdateSlaAvailabilityErrorComponent | ApiV1KubernetesAddonsUpdateSlaTargetErrorComponent |
            ApiV1KubernetesAddonsUpdateSloAvailabilityErrorComponent | ApiV1KubernetesAddonsUpdateSloTargetErrorComponent |
            ApiV1KubernetesAddonsUpdateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAddonsUpdateTemplateBlockErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAddonsUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponent
        | ApiV1KubernetesAddonsUpdateAnnotationsErrorComponent
        | ApiV1KubernetesAddonsUpdateArchivedAtErrorComponent
        | ApiV1KubernetesAddonsUpdateArchivedErrorComponent
        | ApiV1KubernetesAddonsUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesAddonsUpdateBlockNameErrorComponent
        | ApiV1KubernetesAddonsUpdateCatalogueAppErrorComponent
        | ApiV1KubernetesAddonsUpdateCriticalityErrorComponent
        | ApiV1KubernetesAddonsUpdateDebugModeErrorComponent
        | ApiV1KubernetesAddonsUpdateDefaultBlockConfigTemplateErrorComponent
        | ApiV1KubernetesAddonsUpdateDefaultVersionErrorComponent
        | ApiV1KubernetesAddonsUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAddonsUpdateDisplayNameErrorComponent
        | ApiV1KubernetesAddonsUpdateEnforcementErrorComponent
        | ApiV1KubernetesAddonsUpdateIsDefaultErrorComponent
        | ApiV1KubernetesAddonsUpdateKindErrorComponent
        | ApiV1KubernetesAddonsUpdateLabelsErrorComponent
        | ApiV1KubernetesAddonsUpdateNameErrorComponent
        | ApiV1KubernetesAddonsUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAddonsUpdateOrderErrorComponent
        | ApiV1KubernetesAddonsUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesAddonsUpdateProviderErrorComponent
        | ApiV1KubernetesAddonsUpdateProviderIdErrorComponent
        | ApiV1KubernetesAddonsUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesAddonsUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAddonsUpdateScopeErrorComponent
        | ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponent
        | ApiV1KubernetesAddonsUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAddonsUpdateSlaTargetErrorComponent
        | ApiV1KubernetesAddonsUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesAddonsUpdateSloTargetErrorComponent
        | ApiV1KubernetesAddonsUpdateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAddonsUpdateTemplateBlockErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_addons_update_actual_availability_error_component import (
            ApiV1KubernetesAddonsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_allow_multiple_error_component import (
            ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_annotations_error_component import (
            ApiV1KubernetesAddonsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_archived_at_error_component import (
            ApiV1KubernetesAddonsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_archived_error_component import (
            ApiV1KubernetesAddonsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_archived_reason_error_component import (
            ApiV1KubernetesAddonsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_block_name_error_component import (
            ApiV1KubernetesAddonsUpdateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_catalogue_app_error_component import (
            ApiV1KubernetesAddonsUpdateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_criticality_error_component import (
            ApiV1KubernetesAddonsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_debug_mode_error_component import (
            ApiV1KubernetesAddonsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_default_block_config_template_error_component import (
            ApiV1KubernetesAddonsUpdateDefaultBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_default_version_error_component import (
            ApiV1KubernetesAddonsUpdateDefaultVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_discovery_enabled_error_component import (
            ApiV1KubernetesAddonsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_display_name_error_component import (
            ApiV1KubernetesAddonsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_is_default_error_component import (
            ApiV1KubernetesAddonsUpdateIsDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_kind_error_component import (
            ApiV1KubernetesAddonsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_labels_error_component import (
            ApiV1KubernetesAddonsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_name_error_component import (
            ApiV1KubernetesAddonsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_non_field_errors_error_component import (
            ApiV1KubernetesAddonsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_order_error_component import (
            ApiV1KubernetesAddonsUpdateOrderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_platform_service_error_component import (
            ApiV1KubernetesAddonsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_provider_error_component import (
            ApiV1KubernetesAddonsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_provider_id_error_component import (
            ApiV1KubernetesAddonsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_provider_reference_error_component import (
            ApiV1KubernetesAddonsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_scope_error_component import (
            ApiV1KubernetesAddonsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_scope_expressions_error_component import (
            ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_sla_availability_error_component import (
            ApiV1KubernetesAddonsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_sla_target_error_component import (
            ApiV1KubernetesAddonsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_slo_availability_error_component import (
            ApiV1KubernetesAddonsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_slo_target_error_component import (
            ApiV1KubernetesAddonsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_target_availability_error_component import (
            ApiV1KubernetesAddonsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_template_block_error_component import (
            ApiV1KubernetesAddonsUpdateTemplateBlockErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateBlockNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateDefaultVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateDefaultBlockConfigTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateIsDefaultErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsUpdateOrderErrorComponent):
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
        from ..models.api_v1_kubernetes_addons_update_actual_availability_error_component import (
            ApiV1KubernetesAddonsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_allow_multiple_error_component import (
            ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_annotations_error_component import (
            ApiV1KubernetesAddonsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_archived_at_error_component import (
            ApiV1KubernetesAddonsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_archived_error_component import (
            ApiV1KubernetesAddonsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_archived_reason_error_component import (
            ApiV1KubernetesAddonsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_block_name_error_component import (
            ApiV1KubernetesAddonsUpdateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_catalogue_app_error_component import (
            ApiV1KubernetesAddonsUpdateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_criticality_error_component import (
            ApiV1KubernetesAddonsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_debug_mode_error_component import (
            ApiV1KubernetesAddonsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_default_block_config_template_error_component import (
            ApiV1KubernetesAddonsUpdateDefaultBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_default_version_error_component import (
            ApiV1KubernetesAddonsUpdateDefaultVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_discovery_enabled_error_component import (
            ApiV1KubernetesAddonsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_display_name_error_component import (
            ApiV1KubernetesAddonsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_enforcement_error_component import (
            ApiV1KubernetesAddonsUpdateEnforcementErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_is_default_error_component import (
            ApiV1KubernetesAddonsUpdateIsDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_kind_error_component import (
            ApiV1KubernetesAddonsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_labels_error_component import (
            ApiV1KubernetesAddonsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_name_error_component import (
            ApiV1KubernetesAddonsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_non_field_errors_error_component import (
            ApiV1KubernetesAddonsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_order_error_component import (
            ApiV1KubernetesAddonsUpdateOrderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_platform_service_error_component import (
            ApiV1KubernetesAddonsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_provider_error_component import (
            ApiV1KubernetesAddonsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_provider_id_error_component import (
            ApiV1KubernetesAddonsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_provider_reference_error_component import (
            ApiV1KubernetesAddonsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_scope_error_component import (
            ApiV1KubernetesAddonsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_scope_expressions_error_component import (
            ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_sla_availability_error_component import (
            ApiV1KubernetesAddonsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_sla_target_error_component import (
            ApiV1KubernetesAddonsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_slo_availability_error_component import (
            ApiV1KubernetesAddonsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_slo_target_error_component import (
            ApiV1KubernetesAddonsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_target_availability_error_component import (
            ApiV1KubernetesAddonsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_update_template_block_error_component import (
            ApiV1KubernetesAddonsUpdateTemplateBlockErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAddonsUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponent
                | ApiV1KubernetesAddonsUpdateAnnotationsErrorComponent
                | ApiV1KubernetesAddonsUpdateArchivedAtErrorComponent
                | ApiV1KubernetesAddonsUpdateArchivedErrorComponent
                | ApiV1KubernetesAddonsUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesAddonsUpdateBlockNameErrorComponent
                | ApiV1KubernetesAddonsUpdateCatalogueAppErrorComponent
                | ApiV1KubernetesAddonsUpdateCriticalityErrorComponent
                | ApiV1KubernetesAddonsUpdateDebugModeErrorComponent
                | ApiV1KubernetesAddonsUpdateDefaultBlockConfigTemplateErrorComponent
                | ApiV1KubernetesAddonsUpdateDefaultVersionErrorComponent
                | ApiV1KubernetesAddonsUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAddonsUpdateDisplayNameErrorComponent
                | ApiV1KubernetesAddonsUpdateEnforcementErrorComponent
                | ApiV1KubernetesAddonsUpdateIsDefaultErrorComponent
                | ApiV1KubernetesAddonsUpdateKindErrorComponent
                | ApiV1KubernetesAddonsUpdateLabelsErrorComponent
                | ApiV1KubernetesAddonsUpdateNameErrorComponent
                | ApiV1KubernetesAddonsUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAddonsUpdateOrderErrorComponent
                | ApiV1KubernetesAddonsUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesAddonsUpdateProviderErrorComponent
                | ApiV1KubernetesAddonsUpdateProviderIdErrorComponent
                | ApiV1KubernetesAddonsUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesAddonsUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAddonsUpdateScopeErrorComponent
                | ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponent
                | ApiV1KubernetesAddonsUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAddonsUpdateSlaTargetErrorComponent
                | ApiV1KubernetesAddonsUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesAddonsUpdateSloTargetErrorComponent
                | ApiV1KubernetesAddonsUpdateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAddonsUpdateTemplateBlockErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_0 = (
                        ApiV1KubernetesAddonsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_1 = (
                        ApiV1KubernetesAddonsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_2 = (
                        ApiV1KubernetesAddonsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_3 = (
                        ApiV1KubernetesAddonsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_4 = (
                        ApiV1KubernetesAddonsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_5 = (
                        ApiV1KubernetesAddonsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_6 = (
                        ApiV1KubernetesAddonsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_7 = (
                        ApiV1KubernetesAddonsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_8 = (
                        ApiV1KubernetesAddonsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_9 = (
                        ApiV1KubernetesAddonsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_10 = (
                        ApiV1KubernetesAddonsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_11 = (
                        ApiV1KubernetesAddonsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_12 = (
                        ApiV1KubernetesAddonsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_13 = (
                        ApiV1KubernetesAddonsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_14 = (
                        ApiV1KubernetesAddonsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_15 = (
                        ApiV1KubernetesAddonsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_16 = (
                        ApiV1KubernetesAddonsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_17 = (
                        ApiV1KubernetesAddonsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_18 = (
                        ApiV1KubernetesAddonsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_19 = (
                        ApiV1KubernetesAddonsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_20 = (
                        ApiV1KubernetesAddonsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_21 = (
                        ApiV1KubernetesAddonsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_22 = (
                        ApiV1KubernetesAddonsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_23 = (
                        ApiV1KubernetesAddonsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_24 = (
                        ApiV1KubernetesAddonsUpdateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_25 = (
                        ApiV1KubernetesAddonsUpdateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_26 = (
                        ApiV1KubernetesAddonsUpdateDefaultVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_27 = (
                        ApiV1KubernetesAddonsUpdateDefaultBlockConfigTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_28 = (
                        ApiV1KubernetesAddonsUpdateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_29 = (
                        ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_30 = (
                        ApiV1KubernetesAddonsUpdateIsDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_31 = (
                        ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_update_error_type_32 = (
                        ApiV1KubernetesAddonsUpdateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_addons_update_error_type_33 = (
                    ApiV1KubernetesAddonsUpdateEnforcementErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_addons_update_error_type_33

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_addons_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_addons_update_validation_error.additional_properties = d
        return api_v1_kubernetes_addons_update_validation_error

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
